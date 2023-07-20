import {Box, Button, DialogBody, DialogFooter, Dialog} from '@dagster-io/ui';
import * as React from 'react';

import {PythonErrorInfo} from '../app/PythonErrorInfo';
import {PythonErrorFragment} from '../app/types/PythonErrorFragment.types';

interface Props {
  location: string;
  isOpen: boolean;
  error: PythonErrorFragment | {message: string} | null;
  reloading: boolean;
  onDismiss: () => void;
  onTryReload: () => void;
}

export const RepositoryLocationErrorDialog: React.FC<Props> = (props) => {
  const {isOpen, error, location, reloading, onTryReload, onDismiss} = props;
  return (
    <Dialog
      icon="error"
      title="Erro de localização do código"
      isOpen={isOpen}
      canEscapeKeyClose={false}
      canOutsideClickClose={false}
      style={{width: '90%'}}
    >
      <DialogBody>
        <ErrorContents location={location} error={error} />
      </DialogBody>
      <DialogFooter>
        <Button onClick={onTryReload} loading={reloading} intent="primary">
          Recarregar
        </Button>
        <Button onClick={onDismiss}>Sair</Button>
      </DialogFooter>
    </Dialog>
  );
};

export const RepositoryLocationNonBlockingErrorDialog: React.FC<Props> = (props) => {
  const {isOpen, error, location, reloading, onTryReload, onDismiss} = props;
  return (
    <Dialog
      icon="error"
      title="Erro de localização do código"
      isOpen={isOpen}
      style={{width: '90%'}}
      onClose={onDismiss}
    >
      <DialogBody>
        <ErrorContents location={location} error={error} />
      </DialogBody>
      <DialogFooter>
        <Button onClick={onTryReload} loading={reloading} intent="primary">
          Recarregar
        </Button>
        <Button onClick={onDismiss}>Sair</Button>
      </DialogFooter>
    </Dialog>
  );
};

const ErrorContents: React.FC<{
  location: string;
  error: PythonErrorFragment | {message: string} | null;
}> = ({location, error}) => (
  <>
    <Box margin={{bottom: 12}}>
      Erro a carregar <strong>{location}</strong>. Tente recarregar o local do código depois de resolver o problema.
    </Box>
    {error ? <PythonErrorInfo error={error} /> : null}
  </>
);
