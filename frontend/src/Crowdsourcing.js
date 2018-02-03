import React from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import ProjectsGrid from './ProjectsGrid';

import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import Button from 'material-ui/Button';
import IconButton from 'material-ui/IconButton';
import MenuIcon from 'material-ui-icons/Menu';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';

const styles = {
    root: {
      width: '100%',
    },
    flex: {
      flex: 1,
    },
    menuButton: {
      marginLeft: -12,
      marginRight: 20,
    },
  };

const Crowdsourcing = () => (
    <div className={styles.root}>
    <AppBar position="static" color="primary">
        <Toolbar>
          <IconButton className={styles.menuButton} color="inherit" aria-label="Menu">
            <MenuIcon />
          </IconButton>
          <Typography type="title" color="inherit" className={styles.flex}>
            Magento Community Engineering Crowdsourcing
          </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
    <ProjectsGrid />
    </div>

);

export default Crowdsourcing;

