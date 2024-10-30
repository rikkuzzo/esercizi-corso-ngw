import React, { useEffect, useState } from 'react';

function PrezzoCriptovaluta() {
  const [prezzo, setPrezzo] = useState(0);

  useEffect(() => {
    const fetchPrezzoCriptovaluta = () => {
      const nuovoPrezzo = (Math.random() * 10000).toFixed(2);
      setPrezzo(nuovoPrezzo);
    };

    fetchPrezzoCriptovaluta();
    const intervallo = setInterval(fetchPrezzoCriptovaluta, 60000);

    return () => clearInterval(intervallo);
  }, []);

  return (
    <div className="prezzo-criptovaluta">
      <h2>Prezzo Criptovaluta: ${prezzo}</h2>
    </div>
  );
}

export default PrezzoCriptovaluta;
