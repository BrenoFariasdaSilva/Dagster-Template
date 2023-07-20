import {Alert, Box} from '@dagster-io/ui';
import * as React from 'react';

import {DaemonHealthFragment} from '../instance/types/DaemonList.types';

type Props = React.ComponentPropsWithRef<typeof Box> & {
  daemonHealth: DaemonHealthFragment | undefined;
};

export const SchedulerInfo: React.FC<Props> = ({daemonHealth, ...boxProps}) => {
  let healthy = undefined;

  if (daemonHealth) {
    const schedulerHealths = daemonHealth.allDaemonStatuses.filter(
      (daemon) => daemon.daemonType === 'SCHEDULER',
    );
    if (schedulerHealths) {
      const schedulerHealth = schedulerHealths[0];
      healthy = !!(schedulerHealth.required && schedulerHealth.healthy);
    }
  }

  if (healthy === false) {
    return (
      <Box {...boxProps}>
        <Alert
          intent="warning"
          title="O daemon do programador não está sendo executado."
          description={
            <div>
               Consulte a documentação{' '}
              <a href="https://docs.dagster.io/deployment/dagster-daemon">
                dagster-daemon documentation
              </a>{' '}
               para obter mais informações sobre como implantar o processo do dagster-daemon.
            </div>
          }
        />
      </Box>
    );
  }

  return null;
};
