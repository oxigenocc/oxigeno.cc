import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect
  } from "react-router-dom";
import App from '../App';
import { FormularioDist } from '../Componentes/FormularioDist';

export const AppRouter = () => {
    return (
        <Router>
            <div>    
                <Switch>
                    <Route exact path="/formulario" component={FormularioDist} />
                    <Route exact path="/"           component={App} />
                    <Redirect to="/" />
                </Switch>
            </div>
        </Router>
    )
}
