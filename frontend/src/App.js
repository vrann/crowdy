import React from 'react';
import Crowdsourcing from './Crowdsourcing'
import Chart from './Chart'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'


const App = () => (
  <Router>
    <div>
      <ul>
        <li><Link to="">Home</Link></li>
        <li><Link to="crowdsourcing">Crowdsourcing</Link></li>
        <li><Link to="chart">Chart</Link></li>
      </ul>

      <hr/>

      <Route exact path="" component={Crowdsourcing}/>
      <Route path="chart" component={Chart}/>
    </div>
  </Router>
)
export default App