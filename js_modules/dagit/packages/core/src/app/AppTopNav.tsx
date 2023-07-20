import {Box, Colors, Icon, IconWrapper, Tooltip} from '@dagster-io/ui';
import * as React from 'react';
import {Link, NavLink, useHistory} from 'react-router-dom';
import styled from 'styled-components/macro';
import logo from '../../../app/public/logo.png';
import {DeploymentStatusIcon} from '../nav/DeploymentStatusIcon';
import {VersionNumber} from '../nav/VersionNumber';
import {SearchDialog} from '../search/SearchDialog';

import {LayoutContext} from './LayoutProvider';
import {ShortcutHandler} from './ShortcutHandler';
import {WebSocketStatus} from './WebSocketProvider';

type AppNavLinkType = {
  title: string;
  element: React.ReactNode;
};
interface Props {
  children?: React.ReactNode;
  searchPlaceholder: string;
  rightOfSearchBar?: React.ReactNode;
  showStatusWarningIcon?: boolean;
  getNavLinks?: (navItems: AppNavLinkType[]) => React.ReactNode;
}

export const AppTopNav: React.FC<Props> = ({
  children,
  rightOfSearchBar,
  searchPlaceholder,
  getNavLinks,
}) => {
  const history = useHistory();

  const navLinks = () => {
    return [
      {
        title: 'overview',
        element: (
          <ShortcutHandler
            key="overview"
            onShortcut={() => history.push('/overview')}
            shortcutLabel="⌥1"
            shortcutFilter={(e) => e.altKey && e.code === 'Digit1'}
          >
            <TopNavLink to="/overview" data-cy="AppTopNav_StatusLink">
              Visão Geral
            </TopNavLink>
          </ShortcutHandler>
        ),
      },
      {
        title: 'runs',
        element: (
          <ShortcutHandler
            key="runs"
            onShortcut={() => history.push('/runs')}
            shortcutLabel="⌥2"
            shortcutFilter={(e) => e.altKey && e.code === 'Digit2'}
          >
            <TopNavLink to="/runs" data-cy="AppTopNav_RunsLink">
              Executar
            </TopNavLink>
          </ShortcutHandler>
        ),
      },
      {
        title: 'assets',
        element: (
          <ShortcutHandler
            key="assets"
            onShortcut={() => history.push('/assets')}
            shortcutLabel="⌥3"
            shortcutFilter={(e) => e.altKey && e.code === 'Digit3'}
          >
            <TopNavLink
              to="/assets"
              data-cy="AppTopNav_AssetsLink"
              isActive={(_, location) => {
                const {pathname} = location;
                return pathname.startsWith('/assets') || pathname.startsWith('/asset-groups');
              }}
              exact={false}
            >
              Ativos
            </TopNavLink>
          </ShortcutHandler>
        ),
      },
      {
        title: 'deployment',
        element: (
          <ShortcutHandler
            key="deployment"
            onShortcut={() => history.push('/locations')}
            shortcutLabel="⌥4"
            shortcutFilter={(e) => e.altKey && e.code === 'Digit4'}
          >
            <TopNavLink
              to="/locations"
              data-cy="AppTopNav_StatusLink"
              isActive={(_, location) => {
                const {pathname} = location;
                return (
                  pathname.startsWith('/locations') ||
                  pathname.startsWith('/health') ||
                  pathname.startsWith('/config')
                );
              }}
            >
              <Box flex={{direction: 'row', alignItems: 'center', gap: 6}}>
                Implantação
                <DeploymentStatusIcon />
              </Box>
            </TopNavLink>
          </ShortcutHandler>
        ),
      },
    ];
  };

  return (
    <AppTopNavContainer>
      <Box flex={{direction: 'row', alignItems: 'center', gap: 16}}>
        <AppTopNavLogo />
        <Box margin={{left: 8}} flex={{direction: 'row', alignItems: 'center', gap: 16}}>
          {getNavLinks ? getNavLinks(navLinks()) : navLinks().map((link) => link.element)}
        </Box>
        {rightOfSearchBar}
      </Box>
      <Box flex={{direction: 'row', alignItems: 'center'}}>
        <SearchDialog searchPlaceholder={searchPlaceholder} />
        {children}
      </Box>
    </AppTopNavContainer>
  );
};

export const AppTopNavLogo: React.FC = () => {
  const {nav} = React.useContext(LayoutContext);
  const navButton = React.useRef<null | HTMLButtonElement>(null);

  const onToggle = React.useCallback(() => {
    navButton.current && navButton.current.focus();
    nav.isOpen ? nav.close() : nav.open();
  }, [nav]);

  const onKeyDown = React.useCallback(
    (e: React.KeyboardEvent<HTMLButtonElement>) => {
      if (e.key === 'Escape' && nav.isOpen) {
        nav.close();
      }
    },
    [nav],
  );

  return (
    <LogoContainer>
      {nav.canOpen ? (
        <ShortcutHandler
          onShortcut={() => onToggle()}
          shortcutLabel="."
          shortcutFilter={(e) => e.key === '.'}
        >
          <NavButton onClick={onToggle} onKeyDown={onKeyDown} ref={navButton}>
            <Icon name="menu" color={Colors.White} size={24} />
          </NavButton>
        </ShortcutHandler>
      ) : null}
      <Box flex={{display: 'inline-flex'}} margin={{left: 8}}>
        <GhostDaggyWithTooltip />
      </Box>
    </LogoContainer>
  );
};

export const GhostDaggyWithTooltip = () => {
  return (
    <DaggyTooltip
      content={
        <Box flex={{direction: 'row', gap: 4}}>
          <WebSocketStatus />
          <VersionNumber />
        </Box>
      }
      placement="bottom"
      modifiers={{offset: {enabled: true, options: {offset: [0, 18]}}}}
    >
      <Link to="/home">
        <LogoDagster/>
      </Link>
    </DaggyTooltip>
  );
};

const LogoDagster = () => {
 return <img src={logo} alt="Logo" style={{width:100}}/>;
};

const DaggyTooltip = styled(Tooltip)`
  &.bp4-popover2-target {
    display: inline-flex;
  }
`;

export const TopNavLink = styled(NavLink)`
  color: ${Colors.Gray400};
  font-weight: 600;
  transition: color 50ms linear;
  padding: 24px 0;
  text-decoration: none;

  :hover {
    color: ${Colors.Gray300};
  }
    text-decoration: none;

  :active,
  &.active {
    color: ${Colors.White};
    text-decoration: none;
  }

  :focus {
    outline: none !important;
    color: ${Colors.White};
  }
`;

export const AppTopNavContainer = styled.div`
  background: ${Colors.Gray900};
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 64px;
`;

const LogoContainer = styled.div`
  cursor: pointer;
  display: flex;
  align-items: center;
  flex-shrink: 0;
  padding-left: 12px;

  svg {
    transition: filter 100ms;
  }

  &:hover {
    svg {
      filter: brightness(90%);
    }
  }
`;

const NavButton = styled.button`
  border-radius: 20px;
  cursor: pointer;
  margin-left: 4px;
  outline: none;
  padding: 6px;
  border: none;
  background: transparent;
  display: block;

  ${IconWrapper} {
    transition: background 100ms linear;
  }

  :hover ${IconWrapper} {
    background: ${Colors.Gray500};
  }

  :active ${IconWrapper} {
    background: ${Colors.Blue200};
  }

  :focus {
    background: ${Colors.Gray700};
  }
`;
