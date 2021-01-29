import React, { useState, useEffect } from 'react';
import MyCard from "./MyCard.js"
import {useSelector} from "react-redux";
// import data from "../img/data.json";
import CircularProgress from '@material-ui/core/CircularProgress';


export default function CardsGrid(props) { 
  const [data, setData] = useState([]); 
  const [cargado, setCargado] = useState(1); // 0 = error, 1 = cargando, 2 = success
  const state = useSelector( state => state.filtrosAvanzados );  
  const [filteredData, setFilteredData] = useState(data);
  
  const endPoint = window.location.href + "data";

  // console.log(endPoint);
  useEffect(() => {
    async function getData() {
      try {
        const dataPeticion = await fetch(endPoint);
        const dataBase= await dataPeticion.json();
        setData(dataBase);
        setCargado(2);
        // console.log("Success");
        // console.log(dataPeticion);
      } catch (error) {
        setCargado(0);
        // console.log("error")
      }
    }
    getData();

  }, []);
  
  useEffect(() => {

    if( cargado ===2 ){      
 
      let newData = data;
      
      if(state.domicilioSwitch){
        if( newData.distribuidor)
        newData = newData.filter(distribuidor => distribuidor.a_domicilio === true)
      } 
      if(state.tarjetaSwitch){
        newData = newData.filter(distribuidor => distribuidor.pago_con_tarjeta === true)
      }
      if(state.tanqueVenta){
        newData = newData.filter(distribuidor => distribuidor.tanques[0]?.disponibilidad_venta > 0)
      }
      if(state.tanqueRenta){
        newData = newData.filter(distribuidor => distribuidor.tanques[0]?.disponibilidad_renta > 0)
      }
      if(state.tanqueRecarga){
        newData = newData.filter(distribuidor => distribuidor.tanques[0]?.disponibilidad_recarga > 0)
      }
      if(state.concentradorRenta){
        newData = newData.filter(distribuidor => distribuidor.concentradores[0]?.disponibilidad_renta > 0)
      }
      if(state.concentradorVenta){
        newData = newData.filter(distribuidor => distribuidor.concentradores[0]?.disponibilidad_venta > 0)
      }

      setFilteredData(newData)
    }
  }, [state, cargado])
  
  if( cargado === 2 ){
    return (
      <div className="tarjetas-container col-12 col-md-9" >
      { 
        filteredData.map((distribuidor) =>
          <MyCard 
            key={`${distribuidor.nombre_distribuidor}${distribuidor.telefono}`}
            distribuidor = {distribuidor}
          />
        ) 

      } 
      </div>
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
