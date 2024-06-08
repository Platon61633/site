'use client'

import Image from "next/image";
import { useState } from "react";

export default function Home() {

  //---------------input-----------

  const [csvData, setCsvData] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (!file) {
      setErrorMessage('Please select a file.');
      return;
    }
    if (!file.name.endsWith('.csv')) {
      setErrorMessage('Please upload a CSV file.');
      return;
    }
    setIsLoading(true);
    const reader = new FileReader();
    reader.onload = (e) => {
      const text = e.target.result;
      const rows = text.split('\n').map((row) => row.split(','));
      setCsvData(rows);
      setErrorMessage('');
      setIsLoading(false);
    };
    reader.readAsText(file);
  };

  //--------------input------------

  const [Patriotizm , SetPatriotizm] = useState(false);
  

  return (
    <div className="Home">
      {Patriotizm?
      <div className="App">
        <div className="head">
        <div className="russia">
          <div className="white"></div>
          <div className="blue"></div>
          <div className="red"></div>
        </div>
        <div className="flags">
          <img src={'/assets/rostov.jpg'} alt="флаг Ростовской области" width={150} height={75}/>
          <h1>zxcTMOL613</h1>
          <img src={'/assets/tgn.png'} alt='флаг Таганрога' width={75}/>
        </div>
        

      </div>
      <div className="title">
        Анализ результатов полётов
      </div>
      <div className="desc">
        <div>Сайт определяет наличие аномалии GPS, атаки на БПЛА и её тип (асинхронная, синхронная, глушение GPS)</div>
        <div className="line"></div>
      </div>
      <div>
        <div className="Loader-patriotizm">
          <span>Загрузите файл .ulg</span>
          <input type="file" onChange={handleFileUpload} accept=".ulg" />
        </div>
      
      <div onClick={e=>console.log(csvData, errorMessage,isLoading)}>test</div>

      </div>
      </div>
      :
      <div className="App">
        <div className="patriotizm" onClick={()=>SetPatriotizm(true)}>
          патриотичный версия 
        </div>
        <div className="head dron">
          <div className="black-fon">
            <div className="title">
              zxcTMOL613
            </div>
            <div className="desc">
              <div>Сайт определяет наличие аномалии GPS, атаки на БПЛА и её тип (асинхронная, синхронная, глушение GPS)</div>
            </div>
            <main>
            <div className="Loader">
          <input type="file" id="file"/>
          <label for="file" className="button">
          Загрузите файл .ulg
</label>
        </div>
            </main>
          </div>
        </div>
      </div>}
    </div>
  );
}


// main
//         главная: краткое описание что делает
//         залить файл ugl
//         =
//         характеристика
//         как мы поняли
