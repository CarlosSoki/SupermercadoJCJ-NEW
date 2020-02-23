import React from 'react';
import axios from 'axios';

import { Card } from 'antd'

class SucursalesDetail extends React.Component {

    state = {
        sucursales: {}
    }

    componentDidMount(){
        const sucursalesID = this.props.match.params.sucursalesID;
        axios.get(`http://localhost:8000/supermercado/sucursales/${sucursalesID}`)
            .then(res => {
                this.setState({
                    sucursales: res.data
                });
               console.log(res.data);
            })
    }

    render(){
        return(
            <Card title={this.state.sucursales.sucursal}>
                <p>{this.state.sucursales.direccion}</p>
            </Card>
        )
    }
}

export default SucursalesDetail;