import {QueryResult} from '@apollo/client';
import {Box, Tabs} from '@dagster-io/ui';
import * as React from 'react';

import {QueryRefreshCountdown, QueryRefreshState} from '../app/QueryRefresh';
import {TabLink} from '../ui/TabLink';

interface Props<TData> {
  refreshState?: QueryRefreshState;
  queryData?: QueryResult<TData, any>;
  tab: string;
}

export const OverviewTabs = <TData extends Record<string, any>>(props: Props<TData>) => {
  const {refreshState, tab} = props;

  return (
    <Box flex={{direction: 'row', justifyContent: 'space-between', alignItems: 'flex-end'}}>
      <Tabs selectedTabId={tab}>
        <TabLink id="timeline" title="Linha do tempo" to="/overview/timeline" />
        <TabLink id="jobs" title="Empregos" to="/overview/jobs" />
        <TabLink id="schedules" title="Horários" to="/overview/schedules" />
        <TabLink id="sensors" title="Sensores" to="/overview/sensors" />
        <TabLink id="resources" title="Recursos" to="/overview/resources" />
        <TabLink id="backfills" title="Preenchimentos" to="/overview/backfills" />
      </Tabs>
      {refreshState ? (
        <Box padding={{bottom: 8}}>
          <QueryRefreshCountdown refreshState={refreshState} />
        </Box>
      ) : null}
    </Box>
  );
};
