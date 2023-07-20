import {NonIdealState} from '@dagster-io/ui';
import * as React from 'react';

export const AssetsEmptyState = ({prefixPath}: {prefixPath: string[]}) => (
  <NonIdealState
    icon="asset"
    title="Ativos"
    description={
      <p>
        {prefixPath && prefixPath.length
          ? `Não há ativos materializados correspondentes com a chave de ativo especificada. `
          : `Não existem ativos materializados conhecidos. `}
        Qualquer chave de ativo que tenha sido especificada com um <code>Materialização de ativos</code> durante um
        a execução do pipeline aparecerá aqui.
        Veja o {' '}
        <a href="https://docs.dagster.io/_apidocs/ops#dagster.AssetMaterialization">
          Documentação de materialização de ativos
        </a>{' '}
        para maiores informações.
      </p>
    }
  />
);
