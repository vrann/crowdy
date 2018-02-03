import React from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import ProjectCard from './ProjectCard';
import Grid from 'material-ui/Grid';
import Paper from 'material-ui/Paper';
var data = require('../data/projects.json');


class ProjectsGrid extends React.Component {
    
      constructor(props) {
        super(props);
        this.state = data;
      }
    
      componentDidMount() {
        // var _this = this;
        // this.serverRequest = 
        //   axios
        //     .get("http://codepen.io/jobs.json")
        //     .then(function(result) {    
        //       _this.setState({
        //         jobs: result.data.jobs
        //       });
        //     })
      }
    
      componentWillUnmount() {
        //this.serverRequest.abort();
      }
    
      render() {
        return (
          <div style={{ padding: 10 }}>
          
            <Grid container 
            direction='row'
            justify='flex-start'
            alignments='flex-start'
            spacing={8}>
              
                  {this.state.projects.map(function(project) {
                    return (
                      <Grid item >

                          <ProjectCard project={project} />

                      </Grid>  
                    );
                  })}
                
            </Grid>
          </div>  
        )
      }
    }      
    

export default ProjectsGrid;