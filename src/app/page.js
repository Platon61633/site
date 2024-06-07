'use client'

import Image from "next/image";
import { useState } from "react";

export default function Home() {

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

  return (
    <div className="App">
      <div className="title">
        Анализ результатов полётов
      </div>
      <div className="desc">
        Сайт определяет наличие анамалии GPS, атаки на БПЛА и её тип (асинхронная, синхронная, глушение GPS)
      </div>
      <main>
        <div className="Loader">
          <span>Загрузите файл .ulg</span>
          <input type="file" onChange={handleFileUpload} accept=".ulg" />
        </div>
      
      <div onClick={e=>console.log(csvData, errorMessage,isLoading)}>log-----------</div>

      </main>
    </div>
  );
}


// main
//         главная: краткое описание что делает
//         залить файл ugl
//         =
//         характеристика
//         как мы поняли
