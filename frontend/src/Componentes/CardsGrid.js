import React, { useState, useEffect } from 'react';
import MyCard from "./MyCard.js"
import data from '../img/data.json'
import {useSelector} from "react-redux";

export default function CardsGrid(props) {  
  const state = useSelector( state => state.filtrosAvanzados );  
  const [filteredData, setFilteredData] = useState(data)  
  
  useEffect(() => {
    let newData = data
    
    if(state.domicilioSwitch){
      newData = newData.filter(distribuidor => distribuidor.a_domicilio === true)
    } 
    if(state.tarjetaSwitch){
      newData = newData.filter(distribuidor => distribuidor.pago_con_tarjeta === true)
    }
    if(state.tanqueVenta){
      newData = newData.filter(distribuidor => distribuidor.tanques[0].disponibilidad_venta > 0)
    }
    if(state.tanqueRenta){
      newData = newData.filter(distribuidor => distribuidor.tanques[0].disponibilidad_renta > 0)
    }
    if(state.tanqueRecarga){
      newData = newData.filter(distribuidor => distribuidor.tanques[0].disponibilidad_recarga > 0)
    }
    if(state.concentradorRenta){
      newData = newData.filter(distribuidor => distribuidor.concentradores[0].disponibilidad_renta > 0)
    }
    if(state.concentradorVenta){
      newData = newData.filter(distribuidor => distribuidor.concentradores[0].disponibilidad_venta > 0)
    }

    setFilteredData(newData)

  }, [state])
  
  return (
    <div className="tarjetas-container col-12 col-md-9" >
      {filteredData.map((distribuidor) =>
        <MyCard 
          key={distribuidor.nombre_distribuidor}
          distribuidor = {distribuidor}
        />
      )}
      
    </div>
  );
  
}
