import React, { useState } from 'react';
import Card from 'react-bootstrap/Card';
import KeyboardArrowDown from '@material-ui/icons/KeyboardArrowDown';
import KeyboardArrowUp from '@material-ui/icons/KeyboardArrowUp';
import Switch from '@material-ui/core/Switch';
import FormGroup from '@material-ui/core/FormGroup';
import Checkbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import {useDispatch,useSelector} from "react-redux";
import {filtroDomicilio,filtroTarjeta,filtroTanqueVenta,filtroTanqueRenta,filtroTanqueRecarga,filtroConcentradorVenta,filtroConcentradorRenta} from "../actions/filtrosAvanzados";

export const MenuLateral = () =>{

    const dispatch = useDispatch();
    const state = useSelector( state => state.filtrosAvanzados );
    
    const [tanque, setTanque] = useState(false)
    const [concentrador, setConcentrador] = useState(false)
    const [domicilio, setDomicilio] = useState(false)
    const [tarjeta, setTarjeta] = useState(false)
    
    
    const toggle = (id) =>{
        
        switch (id) {
            case 0:
                setTanque(!tanque);
                break;
            case 1: 
                setConcentrador(!concentrador);
                break;
            case 2:
                setDomicilio(!domicilio);
                break;
            case 3: 
                setTarjeta(!tarjeta);
                break;
            default:
                break;
        }
    }

    const cambiarFiltro = (id) => {
        switch (id) {
            case 0:
                dispatch( filtroTanqueVenta(!state.tanqueVenta) );
                break;
            case 1:
                dispatch( filtroTanqueRenta(!state.tanqueRenta) );
                break;
            case 2:
                dispatch( filtroTanqueRecarga(!state.tanqueRecarga) );
                break;
            case 3:
                dispatch( filtroConcentradorVenta(!state.concentradorVenta) );
                break;
            case 4:
                dispatch( filtroConcentradorRenta(!state.concentradorRenta) );
                break;
            case 5:
                dispatch( filtroDomicilio(!state.domicilioSwitch) );
                break;
            case 6:
                dispatch( filtroTarjeta(!state.tarjetaSwitch) );
                break;
        
            default:
                break;
        }
    }

    

    return(
        <div className="menu-lateral-container col-12 col-md-3 hidden-sm">
            <div className="menu-lateral-header">
                Filtros avanzados
            </div>
            <Card style={{ width: '100%' }}>
                <Card.Header onClick={ () => toggle(0) } id="tanque-header">
                    <div className="flecha-texto">
                        Tanques
                    </div>
                    <div className="flecha">
                        { !tanque ? <KeyboardArrowDown /> : <KeyboardArrowUp /> }
                    </div>
                </Card.Header>
                { tanque && 
                    <div className="menu-checkbox">
                        <FormGroup>
                            <FormControlLabel
                                control={<Checkbox color="primary" checked={state.tanqueVenta} onChange={() => cambiarFiltro(0)} name="checkedA" />}
                                label="Venta"
                            />
                            <FormControlLabel
                                control={<Checkbox color="primary" checked={state.tanqueRenta} onChange={() => cambiarFiltro(1) } name="checkedA" />}
                                label="Renta"
                            />
                            <FormControlLabel
                                control={<Checkbox color="primary" checked={state.tanqueRecarga} onChange={() => cambiarFiltro(2) } name="checkedA" />}
                                label="Recarga"
                            />
                        </FormGroup>
                    </div>
                }
            </Card>
            <Card style={{ width: '100%' }}>
                <Card.Header onClick={() => toggle(1) } id="tanque-header">
                    <div className="flecha-texto">
                        Concentradores
                    </div>
                    <div className="flecha">
                        { !concentrador ? <KeyboardArrowDown /> : <KeyboardArrowUp /> }
                    </div>
                </Card.Header>
                { concentrador && 
                    <div className="menu-checkbox">
                        <FormGroup>
                            <FormControlLabel
                                control={<Checkbox color="primary" checked={state.concentradorVenta} onChange={() => cambiarFiltro(3) } name="checkedA" />}
                                label="Venta"
                            />
                            <FormControlLabel
                                control={<Checkbox color="primary" checked={state.concentradorRenta} onChange={() => cambiarFiltro(4) } name="checkedA" />}
                                label="Renta"
                            />
                        </FormGroup>
                    </div>
                }
            </Card>
            <Card style={{ width: '100%' }}>
                <Card.Header onClick={() => toggle(2) } id="tanque-header">
                    <div className="flecha-texto">
                        Servicio a domicilio
                    </div>
                    <div className="flecha">
                        { !domicilio ? <KeyboardArrowDown /> : <KeyboardArrowUp /> }
                    </div>
                </Card.Header>
                
                    { domicilio && 
                        <div className="switch-container">
                            <Switch
                                className="switch"
                                checked={state.domicilioSwitch}
                                onChange={() => cambiarFiltro(5)}
                                name="checkedA"
                                color="primary"
                                inputProps={{ 'aria-label': 'secondary checkbox' }}
                            />
                        </div>
                    }
            </Card>
            <Card style={{ width: '100%' }}>
                <Card.Header onClick={ () => toggle(3) } id="tanque-header">
                    <div className="flecha-texto">
                        Pago con tarjeta
                    </div>
                    <div className="flecha">
                        { !tarjeta ? <KeyboardArrowDown /> : <KeyboardArrowUp /> }
                    </div>
                </Card.Header>
                    { tarjeta && 
                        <div className="switch-container">
                            <Switch
                                checked={state.tarjetaSwitch}
                                onChange={() => cambiarFiltro(6)}
                                name="checkedA"
                                color="primary"
                                inputProps={{ 'aria-label': 'secondary checkbox' }}
                            />
                        </div>
                    }
            </Card>
        </div>
    );
}