import {Box, Button, Group, Icon} from '@dagster-io/ui';
import * as React from 'react';

import {showSharedToaster} from '../app/DomUtils';
import {filterByQuery, GraphQueryItem} from '../app/GraphQueryImpl';
import {DEFAULT_DISABLED_REASON} from '../app/Permissions';
import {LaunchButtonConfiguration, LaunchButtonDropdown} from '../launchpad/LaunchButton';

import {IRunMetadataDict, IStepState} from './RunMetadataProvider';
import {doneStatuses, failedStatuses} from './RunStatuses';
import {DagsterTag} from './RunTag';
import {ReExecutionStyle} from './RunUtils';
import {StepSelection} from './StepSelection';
import {TerminationDialog, TerminationState} from './TerminationDialog';
import {RunFragment, RunPageFragment} from './types/RunFragments.types';
import {useJobAvailabilityErrorForRun} from './useJobAvailabilityErrorForRun';

interface RunActionButtonsProps {
  run: RunPageFragment;
  selection: StepSelection;
  graph: GraphQueryItem[];
  metadata: IRunMetadataDict;
  onLaunch: (style: ReExecutionStyle) => Promise<void>;
}

export const CancelRunButton: React.FC<{run: RunFragment}> = ({run}) => {
  const {id: runId, canTerminate} = run;
  const [showDialog, setShowDialog] = React.useState<boolean>(false);
  const closeDialog = React.useCallback(() => setShowDialog(false), []);

  const onComplete = React.useCallback(
    async (terminationState: TerminationState) => {
      const {errors} = terminationState;
      const error = runId && errors[runId];
      if (error && 'message' in error) {
        await showSharedToaster({
          message: error.message,
          icon: 'error',
          intent: 'danger',
        });
      }
    },
    [runId],
  );

  if (!runId) {
    return null;
  }

  return (
    <>
      <Button
        icon={<Icon name="cancel" />}
        intent="danger"
        disabled={showDialog}
        onClick={() => setShowDialog(true)}
      >
        Terminate
      </Button>
      <TerminationDialog
        isOpen={showDialog}
        onClose={closeDialog}
        onComplete={onComplete}
        selectedRuns={{[runId]: canTerminate}}
      />
    </>
  );
};

function stepSelectionWithState(selection: StepSelection, metadata: IRunMetadataDict) {
  const stepStates = selection.keys.map(
    (key) => (key && metadata.steps[key]?.state) || IStepState.PREPARING,
  );

  return {
    ...selection,
    present: selection.keys.length > 0,
    failed: selection.keys.length && stepStates.includes(IStepState.FAILED),
    finished: stepStates.every((stepState) =>
      [IStepState.FAILED, IStepState.SUCCEEDED].includes(stepState),
    ),
  };
}

function stepSelectionFromRunTags(
  run: RunFragment,
  graph: GraphQueryItem[],
  metadata: IRunMetadataDict,
) {
  const tag = run.tags.find((t) => t.key === DagsterTag.StepSelection);
  if (!tag) {
    return null;
  }
  return stepSelectionWithState(
    {keys: filterByQuery(graph, tag.value).all.map((k) => k.name), query: tag.value},
    metadata,
  );
}

export const canRunAllSteps = (run: RunFragment) => doneStatuses.has(run.status);
export const canRunFromFailure = (run: RunFragment) =>
  run.executionPlan && failedStatuses.has(run.status);

export const RunActionButtons: React.FC<RunActionButtonsProps> = (props) => {
  const {metadata, graph, onLaunch, run} = props;
  const artifactsPersisted = run?.executionPlan?.artifactsPersisted;
  const jobError = useJobAvailabilityErrorForRun(run);

  const selection = stepSelectionWithState(props.selection, metadata);

  const currentRunSelection = stepSelectionFromRunTags(run, graph, metadata);
  const currentRunIsFromFailure = run.tags?.some(
    (t) => t.key === DagsterTag.IsResumeRetry && t.value === 'true',
  );

  const full: LaunchButtonConfiguration = {
    icon: 'cached',
    scope: '*',
    title: 'Todos os passos da execução de raiz',
    tooltip: 'Reexecutar a execução do pipeline a partir do zero',
    disabled: !canRunAllSteps(run),
    onClick: () => onLaunch({type: 'all'}),
  };

  const same: LaunchButtonConfiguration = {
    icon: 'linear_scale',
    scope: currentRunSelection?.query || '*',
    title: 'Os mesmos passos',
    disabled: !currentRunSelection || !(currentRunSelection.finished || currentRunSelection.failed),
    tooltip: (
      <div>
        {!currentRunSelection || !currentRunSelection.present
          ? 'Reexecuta o mesmo subconjunto de etapas utilizado para esta execução, caso exista.'
          : !currentRunSelection.finished
          ? 'Aguardar que todos os passos terminem para voltar a executar o mesmo subconjunto.'
          : 'e-executar o mesmo subconjunto de etapas utilizado para esta execução:'}
        <StepSelectionDescription selection={currentRunSelection} />
      </div>
    ),
    onClick: () => onLaunch({type: 'selection', selection: currentRunSelection!}),
  };

  const selected: LaunchButtonConfiguration = {
    icon: 'op',
    scope: selection.query,
    title: selection.keys.length > 1 ? 'Selecionar passos' : 'Selecionar passo',
    disabled: !selection.present || !(selection.finished || selection.failed),
    tooltip: (
      <div>
        {!selection.present
          ? 'Selecionar uma etapa ou digitar um subconjunto de etapas para reexecutar.'
          : !selection.finished
          ? 'Aguarde que os passos terminem para os voltar a executar.'
          : 'Executar novamente as etapas seleccionadas com a configuração existente:'}
        <StepSelectionDescription selection={selection} />
      </div>
    ),
    onClick: () => onLaunch({type: 'selection', selection}),
  };

  const fromSelected: LaunchButtonConfiguration = {
    icon: 'arrow_forward',
    title: 'Selecionar',
    disabled: !canRunAllSteps(run) || selection.keys.length !== 1,
    tooltip: 'Reexecutar o pipeline a jusante das etapas seleccionadas',
    onClick: () => {
      if (!run.executionPlan) {
        console.warn('O plano de execução deve estar presente para iniciar a execução a partir da seleção');
        return Promise.resolve();
      }
      const selectionAndDownstreamQuery = selection.keys.map((k) => `${k}*`).join(',');
      const selectionKeys = filterByQuery(graph, selectionAndDownstreamQuery).all.map(
        (node) => node.name,
      );

      return onLaunch({
        type: 'selection',
        selection: {
          keys: selectionKeys,
          query: selectionAndDownstreamQuery,
        },
      });
    },
  };

  const fromFailureEnabled = canRunFromFailure(run);

  const fromFailure: LaunchButtonConfiguration = {
    icon: 'arrow_forward',
    title: 'Com falhas',
    disabled: !fromFailureEnabled,
    tooltip: !fromFailureEnabled
      ? 'A repetição só é activada quando o pipeline falhou.'
      : 'Tentar novamente a execução do pipeline, ignorando as etapas que foram concluídas com êxito',
    onClick: () => onLaunch({type: 'from-failure'}),
  };

  if (!artifactsPersisted) {
    [selected, same, fromFailure, fromSelected].forEach((option) => {
      option.disabled = true;
      option.title =
        'A repetição e a reexecução só estão ativadas no armazenamento persistente. Tente executar novamente com uma configuração de armazenamento diferente.';
    });
  }

  const options = [full, same, selected, fromSelected, fromFailure];
  const preferredRerun = selection.present
    ? selected
    : fromFailureEnabled && currentRunIsFromFailure
    ? fromFailure
    : currentRunSelection?.present
    ? same
    : null;

  const primary = artifactsPersisted && preferredRerun ? preferredRerun : full;

  const tooltip = () => {
    if (jobError?.tooltip) {
      return jobError?.tooltip;
    }
    return run.hasReExecutePermission ? undefined : DEFAULT_DISABLED_REASON;
  };

  return (
    <Group direction="row" spacing={8}>
      <Box flex={{direction: 'row'}}>
        <LaunchButtonDropdown
          runCount={1}
          primary={primary}
          options={options}
          title={
            primary.scope === '*'
              ? `Re-executar tudo`
              : primary.scope
              ? `Re-executar (${primary.scope})`
              : `Re-executar ${primary.title}`
          }
          tooltip={tooltip()}
          icon={jobError?.icon}
          disabled={jobError?.disabled || !run.hasReExecutePermission}
        />
      </Box>
      {!doneStatuses.has(run.status) ? <CancelRunButton run={run} /> : null}
    </Group>
  );
};

const StepSelectionDescription: React.FC<{selection: StepSelection | null}> = ({selection}) => (
  <div style={{paddingLeft: '10px'}}>
    {(selection?.keys || []).map((step) => (
      <span key={step} style={{display: 'block'}}>{`* ${step}`}</span>
    ))}
  </div>
);
