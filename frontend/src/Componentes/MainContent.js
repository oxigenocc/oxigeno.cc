import React, { useState, useEffect } from 'react';
import  CardsGrid  from "./CardsGrid";
import { MenuLateral } from "./MenuLateral";
import { useSelector } from "react-redux";


export const MainContent = () =>{

    return(
        <div className="main-container col-12">
            <MenuLateral />
            <CardsGrid />
        </div>
    );
}