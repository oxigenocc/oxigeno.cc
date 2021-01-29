import React from 'react';
import ImgBuscador from '../img/advertencia.png';


export const Buscador = () =>{
    // const[activadoEstado,setActivadoEstado]= useState(false);
    // const[activadoCiudad,setActivadoCiudad]= useState(false);
    // const [estado,setEstado]= useState("");
    // const [ciudad,setCiudad]= useState("");

    // const handleSelectEstado=(e)=>{
    //     console.log(e)
    //     setEstado(e);
    //     setActivadoEstado(true);
    // }   
    // const handleSelectCiudad=(e)=>{
    //     console.log(e)
    //     setCiudad(e);
    //     setActivadoCiudad(true);
    // }

    return(
        <div className="Buscador" >
            <div className="buscador-container" >
                <div className="buscador-sombra" >
                    <div className="contenedorBuscar">
                        <div className="ContenedorMenus">                                
                            <div>
                                <p className="texto" >Recuerda solo contratar oxígeno de locales establecidos ademas de hacer uso de este bajo indicación y supervisión médica</p>
                                <span className="correo" >Cualquier duda o comentario contactanos a: </span>
                                <a href="mailto:oxigeno.cc.mx@gmail.com"><span className="correo correoLinea" >oxigeno.cc.mx@gmail.com</span></a>
                            </div>           
                        </div>
                        <div className="BotonBuscar">
                           <img src={ImgBuscador} alt="logo alerta" className="img-fluid" ></img>
                        </div>
                    </div>
                    
                </div>
            </div>
            
        </div>
    );
}