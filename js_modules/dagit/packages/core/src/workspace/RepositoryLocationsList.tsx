import {Box, NonIdealState, Spinner, Table} from '@dagster-io/ui';
import * as React from 'react';

import {CodeLocationRowSet} from './CodeLocationRowSet';
import {WorkspaceContext} from './WorkspaceContext';

export const RepositoryLocationsList = () => {
  const {locationEntries, loading} = React.useContext(WorkspaceContext);

  if (loading && !locationEntries.length) {
    return (
      <Box flex={{gap: 8, alignItems: 'center'}} padding={{horizontal: 24}}>
        <Spinner purpose="body-text" />
        <div>Loading...</div>
      </Box>
    );
  }

  if (!locationEntries.length) {
    return (
      <Box padding={{vertical: 32}}>
        <NonIdealState
          icon="folder"
          title="Nenhum código localizado"
          description="Ao adicionar um local de código, suas definições aparecerão aqui.."
        />
      </Box>
    );
  }

  return (
    <Table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Status</th>
          <th>Atualizado</th>
          <th>Definições</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {locationEntries.map((location) => (
          <CodeLocationRowSet key={location.name} locationNode={location} />
        ))}
      </tbody>
    </Table>
  );
};
