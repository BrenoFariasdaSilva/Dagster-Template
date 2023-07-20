import {FeatureFlag} from './Flags';

/**
 * Open-source feature flags to be displayed in Dagit "User settings"
 */
export const getVisibleFeatureFlagRows = () => [
  {
    key: 'Registro do console de depuração',
    flagType: FeatureFlag.flagDebugConsoleLogging,
  },
  {
    key: 'Desativar WebSockets',
    flagType: FeatureFlag.flagDisableWebsockets,
  },
  {
    key: 'Mostrar recursos na barra lateral de navegação',
    flagType: FeatureFlag.flagSidebarResources,
  },
  {
    key: 'Visualização do calendário experimental/registo de sensores',
    flagType: FeatureFlag.flagSensorScheduleLogging,
  },
  {
    key: 'Visualização experimental de tabelas com filtros',
    flagType: FeatureFlag.flagRunsTableFiltering,
  },
];
