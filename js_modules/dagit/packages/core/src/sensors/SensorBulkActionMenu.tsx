import {Button, Icon, Menu, MenuItem, Popover} from '@dagster-io/ui';
import * as React from 'react';

import {instigationStateSummary} from '../instigation/instigationStateSummary';
import {OpenWithIntent} from '../instigation/useInstigationStateReducer';

import {SensorInfo, SensorStateChangeDialog} from './SensorStateChangeDialog';

interface Props {
  sensors: SensorInfo[];
  onDone: () => void;
}

export const SensorBulkActionMenu = (props: Props) => {
  const {sensors, onDone} = props;
  const count = sensors.length;

  const [openWithIntent, setOpenWithIntent] = React.useState<OpenWithIntent>('not-open');

  const {anyOff, anyOn} = React.useMemo(() => {
    return instigationStateSummary(sensors.map(({sensorState}) => sensorState));
  }, [sensors]);

  return (
    <>
      <Popover
        content={
          <Menu>
            <MenuItem
              text={`Iniciar ${count === 1 ? '1 sensor' : `${count} sensores`}`}
              disabled={!anyOff}
              aria-disabled={!anyOff}
              icon="toggle_on"
              onClick={() => {
                setOpenWithIntent('start');
              }}
            />
            <MenuItem
              text={`Parar ${count === 1 ? '1 sensor' : `${count} sensores`}`}
              disabled={!anyOn}
              aria-disabled={!anyOn}
              icon="toggle_off"
              onClick={() => {
                setOpenWithIntent('stop');
              }}
            />
          </Menu>
        }
        placement="bottom-end"
      >
        <Button disabled={!count} intent="primary" rightIcon={<Icon name="expand_more" />}>
          Carregar
        </Button>
      </Popover>
      <SensorStateChangeDialog
        openWithIntent={openWithIntent}
        sensors={sensors}
        onClose={() => setOpenWithIntent('not-open')}
        onComplete={() => {
          onDone();
        }}
      />
    </>
  );
};
