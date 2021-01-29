import React from 'react';
import  CardsGrid  from "./CardsGrid";
import { MenuLateral } from "./MenuLateral";



export const MainContent = () =>{

    return(
        <div className="main-container col-12">
            <MenuLateral />
            <CardsGrid />
        </div>
    );
}