import {gql, RefetchQueriesFunction, useMutation} from '@apollo/client';
import {Button, DialogBody, DialogFooter, Dialog, Group} from '@dagster-io/ui';
import * as React from 'react';

import {PYTHON_ERROR_FRAGMENT} from '../app/PythonErrorFragment';
import {displayNameForAssetKey} from '../asset-graph/Utils';

import {AssetWipeMutation, AssetWipeMutationVariables} from './types/AssetWipeDialog.types';

interface AssetKey {
  path: string[];
}

export const AssetWipeDialog: React.FC<{
  assetKeys: AssetKey[];
  isOpen: boolean;
  onClose: () => void;
  onComplete: (assetKeys: AssetKey[]) => void;
  requery?: RefetchQueriesFunction;
}> = ({assetKeys, isOpen, onClose, onComplete, requery}) => {
  const [requestWipe] = useMutation<AssetWipeMutation, AssetWipeMutationVariables>(
    ASSET_WIPE_MUTATION,
    {
      variables: {assetKeys: assetKeys.map((key) => ({path: key.path || []}))},
      refetchQueries: requery,
    },
  );

  const wipe = async () => {
    if (!assetKeys.length) {
      return;
    }
    await requestWipe();
    onComplete(assetKeys);
  };

  return (
    <Dialog isOpen={isOpen} title="Limpar as materializações" onClose={onClose} style={{width: 600}}>
      <DialogBody>
        <Group direction="column" spacing={16}>
          <div>Tem certeza de que deseja limpar as materializações para esses imobilizados?</div>
          <ul style={{paddingLeft: 32, margin: 0}}>
            {assetKeys.map((assetKey) => {
              const name = displayNameForAssetKey(assetKey);
              return (
                <li style={{marginBottom: 4}} key={name}>
                  {name}
                </li>
              );
            })}
          </ul>
          <div>
          Os ativos definidos apenas pelas suas materializações históricas desaparecerão do Catálogo de ativos. Os ativos definidos por software permanecerão, a menos que sua definição também seja eliminada..
          </div>
          <strong>Esta ação não pode ser anulada.</strong>
        </Group>
      </DialogBody>
      <DialogFooter topBorder>
        <Button intent="none" onClick={onClose}>
          Cancelar
        </Button>
        <Button intent="danger" onClick={wipe}>
          Limpar
        </Button>
      </DialogFooter>
    </Dialog>
  );
};

const ASSET_WIPE_MUTATION = gql`
  mutation AssetWipeMutation($assetKeys: [AssetKeyInput!]!) {
    wipeAssets(assetKeys: $assetKeys) {
      ... on AssetWipeSuccess {
        assetKeys {
          path
        }
      }
      ...PythonErrorFragment
    }
  }

  ${PYTHON_ERROR_FRAGMENT}
`;
