import React from 'react';
import Sucursales from '../components/sucursales';
import axios from 'axios';

class SucursalesList extends React.Component {

    state = {
        sucursales: []
    }

    componentDidMount(){
        axios.get('http://localhost:8000/supermercado/sucursales/')
            .then(res => {
                this.setState({
                    sucursales: res.data
                });
               console.log(res.data);
            })
    }

    render(){
        return(
            <Sucursales data={this.state.sucursales} />
        )
    }
}

export default SucursalesList;