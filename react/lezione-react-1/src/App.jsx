import React, { useState } from 'react';
import IconeIntestazione from './IconeIntestazione';
import PrezzoCriptovaluta from './PrezzoCriptovaluta';
import MorraCinese from './MorraCinese';
import TabellonePunteggi from './TabellonePunteggi';
import './App.css';

function App() {
  const [sceltaUtente, setSceltaUtente] = useState('');
  const [sceltaSistema, setSceltaSistema] = useState('');
  const [punteggio, setPunteggio] = useState({ utente: 0, sistema: 0 });

  return (
    <div className="App">
      <IconeIntestazione />
      <div className="contenuto-principale">
        <div className="sezione-criptovaluta">
          <PrezzoCriptovaluta />
        </div>
        <div className="sezione-gioco">
          <MorraCinese 
            sceltaUtente={sceltaUtente} 
            setSceltaUtente={setSceltaUtente} 
            sceltaSistema={sceltaSistema} 
            setSceltaSistema={setSceltaSistema} 
            setPunteggio={setPunteggio} 
          />
          <TabellonePunteggi punteggio={punteggio} />
        </div>
      </div>
    </div>
  );
}

export default App;
