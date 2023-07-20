import {Alert, Box} from '@dagster-io/ui';
import * as React from 'react';

import {DaemonHealthFragment} from '../instance/types/DaemonList.types';

type Props = React.ComponentPropsWithRef<typeof Box> & {
  daemonHealth: DaemonHealthFragment | undefined;
};

export const SensorInfo: React.FC<Props> = ({daemonHealth, ...boxProps}) => {
  let healthy = undefined;

  if (daemonHealth) {
    const sensorHealths = daemonHealth.allDaemonStatuses.filter(
      (daemon) => daemon.daemonType === 'SENSOR',
    );
    if (sensorHealths) {
      const sensorHealth = sensorHealths[0];
      healthy = !!(sensorHealth.required && sensorHealth.healthy);
    }
  }

  if (healthy === false) {
    return (
      <Box {...boxProps}>
        <Alert
          intent="warning"
          title="O sensor daemon não esta sendo executado."
          description={
            <div>
             Consulte a documentação{' '}
              <a
                href="https://docs.dagster.io/deployment/dagster-daemon"
                target="_blank"
                rel="noreferrer"
              >
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
