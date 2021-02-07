import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Badge from 'react-bootstrap/Badge';
import CloseIcon from '@material-ui/icons/Close';
import CheckIcon from '@material-ui/icons/Check';
import {dateFormat} from '../helpers/dateFormat';



export default function MyCard(props) { 

  const {
    nombre_distribuidor,
    horario,
    // estado,
    direccion,
    // ciudad,
    a_domicilio,
    pago_con_tarjeta,
    notas,
    telefono,
    ultima_actualizacion,
    concentradores,
    tanques,
    lat,
    lng,
    link_pagina,
    whatsapp
  }= props.distribuidor

  const latMapa= lat? lat:"";
  const lngMapa=lng? lng :"";

  let ofrece_tanque_renta;
  let tanques_renta;

  if ( Object.keys(tanques).length !==0 &&  typeof tanques[0].disponibilidad_renta !== undefined ) {
    tanques_renta=tanques[0].disponibilidad_renta 
    ofrece_tanque_renta = tanques[0].renta
  }else{
    tanques_renta=-1;
    ofrece_tanque_renta=false;
  }; 

  let tanques_venta;
  let ofrece_tanque_venta;

  if (  Object.keys(tanques).length !==0 &&  typeof tanques[0].disponibilidad_venta !== undefined) {
    tanques_venta=tanques[0].disponibilidad_venta
    ofrece_tanque_venta=tanques[0].venta
  }else{
    tanques_venta=-1;
    ofrece_tanque_venta=false;
  }; 

  let tanques_recarga;
  let ofrece_tanques_recarga;

  if (  Object.keys(tanques).length !==0 &&  typeof tanques[0].disponibilidad_recarga !== undefined) {
    tanques_recarga = tanques[0].disponibilidad_recarga
    ofrece_tanques_recarga= tanques[0].recarga
  }else{
    tanques_recarga= -1;
    ofrece_tanques_recarga=false;
  }
  
  let concentradores_renta;
  let ofrece_concentradores_renta;
  if ( Object.keys(concentradores).length !==0 &&  typeof concentradores[0].disponibilidad_renta !== undefined) {
    concentradores_renta = concentradores[0].disponibilidad_renta
    ofrece_concentradores_renta= concentradores[0].renta
  }else{
    concentradores_renta= -1;
    ofrece_concentradores_renta=false;
  }

  let concentradores_venta;
  let ofrece_concentradores_venta;

  if ( Object.keys(concentradores).length !==0 &&typeof concentradores[0].disponibilidad_venta !== undefined) {
    concentradores_venta  = concentradores[0].disponibilidad_venta;
    ofrece_concentradores_venta = concentradores[0].venta
  }else{
    ofrece_concentradores_venta=false;
    concentradores_venta= -1;
  }
  
  

  function disponibilidadPicker(tanques,disponibilidadServicio) {
    let disponibilidad
    if(disponibilidadServicio ===false){
      disponibilidad = <Badge  className="badgeCard" variant="light">N/A</Badge>
    }else if(tanques === 0){
      disponibilidad = <Badge  className="badgeCard" variant="secondary">Sin Disponibilidad</Badge>
    }
    else if(tanques > 0 &&  tanques <= 5){
      disponibilidad = <Badge  className="badgeCard" variant="danger">Baja</Badge>
    }
    else if(tanques > 5 &&  tanques <= 10){
      disponibilidad = <Badge  className="badgeCard" variant="warning">Media</Badge>
    }
    else if(tanques > 10){
      disponibilidad = <Badge  className="badgeCard" variant="success">Alta</Badge>
    }
    else {
      disponibilidad = <Badge  className="badgeCard" variant="primary">Lista de espera</Badge>
    }    
    return disponibilidad    
  }

  return (
    <div className="col-12 col-sm-10 col-md-10 col-lg-6  card-lencho">
      <Card bg={"light"}>
        <Card.Header>
          <small className="text-muted ">Última actualización: {dateFormat(`${ultima_actualizacion}`, "mmm dd yyyy")} a las {dateFormat(`${ultima_actualizacion}`, "HH:MM:ss")} </small>        
        </Card.Header>
        <Card.Body>
          <Card.Title className="card-title">{nombre_distribuidor}</Card.Title>
          <Card.Subtitle className="mt10">Tanques:</Card.Subtitle>
          <Container>          
          <Row className="mt10">
              <Col>
                <Row className="rowBadge">
                  Renta:
                </Row>
                <Row className="rowBadge">
                  {disponibilidadPicker(tanques_renta,ofrece_tanque_renta)}
                </Row>
              </Col>
              <Col>
                <Row className="rowBadge">
                  Venta: 
                </Row>
                <Row className="rowBadge">
                  {disponibilidadPicker(tanques_venta,ofrece_tanque_venta)}
                </Row>
              </Col>
              <Col>
                <Row className="rowBadge">
                  Recarga: 
                </Row>
                <Row className="rowBadge">
                  {disponibilidadPicker(tanques_recarga,ofrece_tanques_recarga)}
                </Row>
              </Col>
            </Row>        
          </Container>
          <br/>
          <Card.Subtitle className="mt10">Concentradores:</Card.Subtitle>
          <Container>          
            <Row className="mt10">
              <Col>
                <Row className="rowBadge">
                  Renta: 
                </Row>
                <Row className="rowBadge">
                  {disponibilidadPicker(concentradores_renta,ofrece_concentradores_renta)}
                </Row>
              </Col>
              <Col>
                <Row className="rowBadge">
                  Venta: 
                </Row>
                <Row className="rowBadge">
                  {disponibilidadPicker(concentradores_venta,ofrece_concentradores_venta)}
                </Row>
              </Col>            
            </Row>          
          </Container>
          
          <br/>
          <Card.Subtitle className="mb-2 text-muted">
            A domicilio:
            {a_domicilio ? <CheckIcon style={{color:"blue"}}/> : <CloseIcon style={{color:"red"}}/>}
          </Card.Subtitle>

          <Card.Subtitle className="text-muted">
            Pago con tarjeta:
            {pago_con_tarjeta ? <CheckIcon style={{color:"blue"}}/> : <CloseIcon style={{color:"red"}}/> }
          </Card.Subtitle>
          <br/>
          <Card.Subtitle className="text-muted">Horario:</Card.Subtitle>
          <p>{horario}</p>
          <Card.Subtitle className="text-muted">Dirección:</Card.Subtitle>
          <p>{direccion}</p>

          <br/>
          <Card.Subtitle className="mb-2 text-muted">Notas:</Card.Subtitle>        
          <Card.Text>
            {notas}
          </Card.Text>
          <Container className="mycard-footer">          
            <Row>
                <Col className="boton-carta link">            
                  <Card.Link href= {link_pagina} target="_blank" rel="noreferrer" >{link_pagina ===null ? "Sin página": "Página Web"}</Card.Link>
                </Col>
                <Col className="boton-carta whatsapp">
                  <Card.Link href={ whatsapp ===null? "#":`https://api.whatsapp.com/send?text=Hola, me gustaría obtener información.&phone=+52${whatsapp}&abid=+52${whatsapp}`} target={ whatsapp === null ? "" : "_blank"} rel="noreferrer">{ 
                    whatsapp === null ? "Sin Whatsapp": "Whatsapp"
                    } </Card.Link>
                </Col>            
              </Row>    
              <Row>
              <Col className="boton-carta map">            
                <Card.Link href= {`https://www.google.com/maps/place/${latMapa},${lngMapa}`} target="_blank" rel="noreferrer" >Mapa</Card.Link>
              </Col>
              <Col className="boton-carta tel">
                <Card.Link href={`tel:${telefono}`}>{ 
                  telefono ===0 || telefono==="0"? "5556581111":telefono
                  } </Card.Link>
              </Col>            
            </Row>         
          </Container>      
        </Card.Body>
        
                
        
      </Card>
    </div>
  );
}
