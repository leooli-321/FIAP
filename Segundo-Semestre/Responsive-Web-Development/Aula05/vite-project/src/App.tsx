import './App.css';
import Componente from './Componente.tsx';

export default function App() {

  const formatar = {
    color: 'white'
  }

  return (
    <>
      <h1 className='titulo'>Wello Horld!</h1>
      <h2 style={formatar}>Isso não é Fiap</h2>
      <Componente/>
    </>
  )
}