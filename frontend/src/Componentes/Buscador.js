import React,{useState } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import  Button from 'react-bootstrap/Button';



export const Buscador = () =>{
    const[activadoEstado,setActivadoEstado]= useState(false);
    const[activadoCiudad,setActivadoCiudad]= useState(false);
    const [estado,setEstado]= useState("");
    const [ciudad,setCiudad]= useState("");

    const handleSelectEstado=(e)=>{
        console.log(e)
        setEstado(e);
        setActivadoEstado(true);
    }   
    const handleSelectCiudad=(e)=>{
        console.log(e)
        setCiudad(e);
        setActivadoCiudad(true);
    }

    return(
        <div className="Buscador" >
            <div className="buscador-container" >
                <div className="buscador-sombra" >
                    <div className="contenedorBuscar">
                        <div className="ContenedorMenus">
                            <div className="BuscadorDropDownEstado dropdown">
                                <Dropdown 
                                    onSelect={handleSelectEstado}
                                >
                                    <Dropdown.Toggle id="dropdown-basic">
                                        {activadoEstado ? estado:'Seleccione Estado' }
                                    </Dropdown.Toggle>
    
                                    <Dropdown.Menu>
                                        <Dropdown.Item id="dropdown-item" eventKey="Ciudad de México">Ciudad de México</Dropdown.Item>
                                    </Dropdown.Menu>
                                </Dropdown>
                            </div>
                            <div className="BuscadorDropDownCiudad">
                                <Dropdown
                                    onSelect={handleSelectCiudad}
                                >
                                    <Dropdown.Toggle variant="primary" id="dropdown-basic" >
                                        {activadoCiudad ? ciudad:'Seleccione Ciudad' }
                                    </Dropdown.Toggle>
    
                                    <Dropdown.Menu id="dropdown-menu" >
                                        <Dropdown.Item id="dropdown-item" eventKey="Álvaro Obregon">Álvaro Obregon</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Benito Juárez">Benito Juárez</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Coyoacán">Coyoacán</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Cuajimalpa">Cuajimalpa</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Cuauhtémoc">Cuauhtémoc</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Gustavo A. Madero">Gustavo A. Madero</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Iztacalco">Iztacalco</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Iztapalapa">Iztapalapa</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Magdalena Contreras">Magdalena Contreras</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Miguel Hidalgo">Miguel Hidalgo</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Milpa Alta">Milpa Alta</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Tláhuac">Tláhuac</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Tlalpan">Tlalpan</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Venustiano Carranza">Venustiano Carranza</Dropdown.Item>
                                        <Dropdown.Item id="dropdown-item" eventKey="Xochimilco">Xochimilco</Dropdown.Item> 
                                    </Dropdown.Menu>
                                </Dropdown>
                            </div>                    
    
                        </div>
                        <div className="BotonBuscar">
                            <Button variant="outline-light"   block>Buscar</Button>
                        </div>
                    </div>
                    
                </div>
            </div>
            
        </div>
    );
}