import React from 'react';
import AddProjectButton from './AddProjectButton'
import Button from 'material-ui/Button';
import TextField from 'material-ui/TextField';
import Chip from 'material-ui/Chip';
import Dialog, {
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from 'material-ui/Dialog';

export default class AddProjetDialog extends React.Component {
    constructor(props) {
      super(props);
      console.log(props)
      this.state = {open: false};
      this.handleClickOpen = this.handleClickOpen.bind(this);
      this.handleClose = this.handleClose.bind(this);
    };
  
    handleClickOpen() {
      this.setState({ open: true });
    };
  
    handleClose() {
      this.setState({ open: false });
    };
  
    render() {
      return (
        <div>
        <AddProjectButton onClick={this.handleClickOpen} />
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">Pledge</DialogTitle>
          <DialogContent>
            <DialogContentText>
              To pledge the hours you'd like to spend
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id="name"
              label="Email Address"
              type="email"
              fullWidth
            />
            <Chip label="10 hours"  />
            <Chip label="20 hours"  />
            <Chip label="50 hours"  />
            <Chip label="1oo %"  />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={this.handleClose} color="primary">
              OK
            </Button>
          </DialogActions>
        </Dialog>
      </div>
      )
    }
}