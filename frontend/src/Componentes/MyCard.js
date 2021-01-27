import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Badge from 'react-bootstrap/Badge';
import CloseIcon from '@material-ui/icons/Close';
import CheckIcon from '@material-ui/icons/Check';
import {dateFormat} from '../helpers/dateFormat'


export default function MyCard(props) { 
  const {
    nombre_distribuidor,
    horario,
    estado,
    direccion,
    ciudad,
    a_domicilio,
    pago_con_tarjeta,
    notas,
    telefono,
    ultima_actualizacion,
    concentradores,
    tanques,
  }= props.distribuidor

  let tanques_renta = tanques[0].disponibilidad_renta
  let tanques_venta = tanques[0].disponibilidad_venta
  let tanques_recarga = tanques[0].disponibilidad_recarga
  
  let concentradores_renta = concentradores[0].disponibilidad_renta
  let concentradores_venta = concentradores[0].disponibilidad_venta
  
  

  function disponibilidadPicker(tanques) {
    let disponibilidad
    if(tanques == 0){
      disponibilidad = <Badge variant="secondary">Sin Disponibilidad{tanques}</Badge>
    }
    else if(tanques > 0 &&  tanques <= 5){
      disponibilidad = <Badge variant="danger">Baja{tanques}</Badge>
    }
    else if(tanques > 5 &&  tanques <= 10){
      disponibilidad = <Badge variant="warning">Media{tanques}</Badge>
    }
    else if(tanques > 10){
      disponibilidad = <Badge variant="success">Alta{tanques}</Badge>
    }
    else{
      disponibilidad = <Badge variant="dark">Sin Información</Badge>
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
          <Card.Subtitle className="text-muted">Tanques:</Card.Subtitle>
          <Container>          
          <Row>
              <Col>
                Renta: {disponibilidadPicker(tanques_renta)}
              </Col>
              <Col>
                Venta: {disponibilidadPicker(tanques_venta)}
              </Col>
              <Col>
                Recarga: {disponibilidadPicker(tanques_recarga)}
              </Col>
            </Row>        
          </Container>
          <br/>
          <Card.Subtitle className="text-muted">Concentradores:</Card.Subtitle>
          <Container>          
            <Row>
              <Col>
                Renta: {disponibilidadPicker(concentradores_renta)}
              </Col>
              <Col>
                Venta: {disponibilidadPicker(concentradores_venta)}
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
          
        </Card.Body>
        
        <Container className="mycard-footer">          
          <Row>
            <Col className="map">            
              <Card.Link href="#" >Mapa</Card.Link>
            </Col>
            <Col className="tel">
              <Card.Link href="#">{telefono}</Card.Link>
            </Col>            
          </Row>          
        </Container>                      
        
      </Card>
    </div>
  );
}
