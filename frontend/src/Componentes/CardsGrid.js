import React, { useState, useEffect } from 'react';
import MyCard from "./MyCard.js"
import {useSelector} from "react-redux";
import CircularProgress from '@material-ui/core/CircularProgress';
import axios from 'axios';
import Pagination from '@material-ui/lab/Pagination';
import {endPoints} from '../types/endPoints';

export default function CardsGrid(props) { 
  const [data, setData] = useState([]); 
  const [cargado, setCargado] = useState(1); // 0 = error, 1 = cargando, 2 = success
  const [inicio,setInicio]=useState(0);
  const state = useSelector( state => state.filtrosAvanzados );  
  const [activePage, setActivePage] = useState(1);


  const handleChange = (event, value) => {
    topFunction();
    setActivePage(value);
  };

  function topFunction() {
    document.body.scrollTop = 100; // For Safari
    document.documentElement.scrollTop = 100; // For Chrome, Firefox, IE and Opera
  }

  const endPoint = `${endPoints}data/`;

  useEffect(() => {
    if( activePage === 1 && inicio===1){
      getData()
    }else{
      setActivePage(1);
    }
  
  }, [state]);


  useEffect(() => {
    setCargado(1)
    getData();
    setInicio(1);
  }, [activePage]);

  async function getData() {
    try {
    
      const dataPeticion = await axios.get(endPoint,{
        params:{
          page: activePage,
          tanqueVenta: state.tanqueVenta ? 1 : "",
          tanqueRecarga: state.tanqueRecarga ? 1 : "",
          tanqueRenta: state.tanqueRenta ? 1 : "",
          concentradorVenta: state.concentradorVenta ? 1 : "",
          concentradorRenta: state.concentradorRenta ? 1 : "",
          pagoConTarjeta: state.tarjetaSwitch ? 1 : "",
          aDomicilio: state.domicilioSwitch ? 1 : "",
          abiertoFin: state.abiertoFin ? 1 : "",
          abierto24: state.abierto24 ? 1 : "",
          gratis: state.gratis ? 1 : "",
          incluirBajas: 0,
        }
      });
      const dataBase= await dataPeticion.data;
      setData(dataBase);
      setCargado(2);
    } catch (error) {
      console.log(error)
      setCargado(0);
    }
  }
  
  
  if( cargado === 2 ){
    return (
      <>
        <div className="tarjetas-container col-12 col-md-9" >
          { 
            data.results.length > 0 
            ?
              data.results.map((distribuidor) =>
                <MyCard 
                  key={`${distribuidor.id}`}
                  distribuidor = {distribuidor}
                />
              ) 
            : 
            <div className="tarjetas-container sinResultados  col-12 col-md-9">
              <div className="cajaSinResultados">
                No se encontraron resultados con estos filtros
              </div>
            </div>
          } 
          <div className="paginacionContainer">
            <Pagination count={Math.ceil(data.count/6)} variant="outlined" color="primary" page={activePage} onChange={handleChange}/>
          </div>
        </div>
      </>
    );
  }else if( cargado === 1){
    return(
      <div className="tarjetas-container circularProgress col-12 col-md-9" >
        <CircularProgress className="circulo" size={100} />
      </div>
    )
  }else{
    return(
      <div className="tarjetas-container error col-12 col-md-9" >
        <div className="cajaError">
          Lo sentimos , hubo un error al cargar los datos (553)
        </div>
      </div>
    )
  }

}
