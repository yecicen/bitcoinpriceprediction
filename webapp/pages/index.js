import Head from 'next/head'
import { useState } from 'react'
import { ResponsiveContainer, LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend } from 'recharts';


let url = 'https://bitcoinpriceprediction-mu.herokuapp.com/api/bitcoin';
export async function getServerSideProps(context) {
  const res = await fetch(url, {
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  })
  let initialData = await res.json()
  initialData = initialData.reverse().slice(-120)
  let diffData = []
  initialData.map(item => {
    item.date = `${item['date'].substring(11, 13)}:${item['date'].substring(14, 16)}`;
    item.price = item['price'].toFixed(3);
    item.prediction = item['prediction'].toFixed(3);
    item['difference'] = Number(Math.abs(Number(item['prediction']) - Number(item['price'])).toFixed(3));
    diffData.push(item['difference'])
  })
  return { props: { initialData } }
}


export default function Home({ initialData }) {
  const [data, setData] = useState(initialData);
  const [darkTheme, setDarkTheme] = useState(false)
  setTimeout(async () => {
    let respond = await fetch(url);
    let newData = await respond.json();

    newData = newData.reverse().slice(-120)
    newData.map(item => {
      item.date = `${item['date'].substring(11, 13)}:${item['date'].substring(14, 16)}`;
      item.price = item['price'].toFixed(3);
      item.prediction = item['prediction'].toFixed(3);
      item['difference'] = Math.abs(item['prediction'] - item['price']).toFixed(3);
    });

    setData(newData);

  }, 60000)

  const handleSwitch = (event) => {
    if (event.target.checked) {
      setDarkTheme(true);
    }
    else {
      setDarkTheme(false);
    }
  }


  return (
    <div className={
      "flex flex-col items-center justify-center min-h-screen py-2 "
      + (darkTheme ? "bg-gray-900" : "")}>
      <Head>
        <title>Bitcoin Price Prediction</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div>
        <div className={"h-20 text-xl text-center " + (darkTheme ? "text-white" : "")}>
          Bitcoin Price Prediction using an LSTM Model
          <div className="switch">
            <div className="theme-switch-wrapper">
              <label className="theme-switch" htmlFor="checkbox">
                <input onChange={handleSwitch} type="checkbox" id="checkbox" />
                <div className="slider round" />
              </label>
            </div>
          </div>
        </div>
      </div>
      <main className="flex flex-col items-center justify-center w-full md:w-2/3 px-5 md:px-20 flex-1 text-center">

        <ResponsiveContainer height={500}>
          <LineChart data={data} className=""
            margin={{ top: 20, right: 10, left: 40, bottom: 10 }}>
            <CartesianGrid strokeDasharray="5 5" />
            <XAxis dataKey="date" />
            <YAxis domain={['dataMin', 'dataMax']} />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="price" stroke="#8884d8" dot={false} />
            <Line type="basis" dataKey="prediction" stroke="#82ca9d" dot={false} />
          </LineChart>
        </ResponsiveContainer>

      </main>

      <footer className={
        "flex items-center justify-center w-full h-24 border-t flex-col "
        + (darkTheme ? "text-white" : "")}>
        <p>Developed by <a href="https://yecicen.dev"> Yunus Emre Çiçen </a></p>
        <a href="https://github.com/yecicen/bitcoinpriceprediction">Click here for the source code</a>
      </footer>
    </div>
  )
}
