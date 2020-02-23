import React from 'react';
import { Route } from 'react-router-dom';

import SucursalesList from './containers/SucursalesListView';
import SucursalesDetail from './containers/SucursalesDetailsView';

const BaseRouter = () => (
    <div> 
        <Route exact path = '/' component={SucursalesList}/>
        <Route exact path = '/:sucursalesID' component={SucursalesDetail}/>
    </div>

);

export default BaseRouter;