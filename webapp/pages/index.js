import Head from 'next/head'
import { useState } from 'react'
import { ResponsiveContainer, LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import CustomTooltip from '../components/customTooltip'
let url = 'https://bitcoinpriceprediction-mu.herokuapp.com/api/bitcoin';
export async function getServerSideProps(context) {
  const res = await fetch(url, {
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  })
  let initialData = await res.json()
  initialData = initialData.slice(-60)
  initialData.map(item => {
    item.date = `${item['date'].substring(11, 13)}:${item['date'].substring(14, 16)}`;
    item.price = item['price'].toFixed(3);
    item.prediction = item['prediction'].toFixed(3);
    item['difference'] = Math.abs(item['prediction'] - item['price']).toFixed(3);
  })
  // initialData = initialData.filter((item) => item.date == date && item.centerId == testcenterID)

  return { props: { initialData } }
}

export default function Home({ initialData }) {
  const [data, setData] = useState(initialData);
  setTimeout(async () => {
      let respond = await fetch(url);
      let newData = await respond.json();

      newData = newData.slice(-60)
      newData.map(item => {
        item.date = `${item['date'].substring(11, 13)}:${item['date'].substring(14, 16)}`;
        item.price = item['price'].toFixed(3);
        item.prediction = item['prediction'].toFixed(3);
        item['difference'] = Math.abs(item['prediction'] - item['price']).toFixed(3);
      });

      setData(newData);
    
  }, 60000)
  console.log(data);
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-gray-900">
      <Head>
        <title>Bitcoin Price Prediction</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1 className="h-20 text-xl text-white text-center">Bitcoin Price Prediction using LSTM Model</h1>
      <main className="flex flex-col items-center justify-center w-full md:w-2/3 px-5 md:px-20 flex-1 text-center">

        <ResponsiveContainer height={500}>
          <LineChart data={data} className="bg-gray-800"
            margin={{ top: 20, right: 10, left: 40, bottom: 10 }}>
            <CartesianGrid strokeDasharray="5 5" />
            <XAxis dataKey="date" />
            <YAxis domain={['dataMin', 'dataMax']} />
            <Tooltip />
            {/* <Tooltip content={<CustomTooltip />} /> */}
            <Line type="monotone" dataKey="price" stroke="#8884d8" />
            <Line type="basis" dataKey="prediction" stroke="#82ca9d" />
            {/* <Line type="basis" dataKey="difference" stroke="#eba959" /> */}
            {/* <Line type="step" dataKey="source" stroke="red" /> */}
          </LineChart>
        </ResponsiveContainer>

      </main>

      <footer className="flex items-center justify-center w-full h-24 border-t text-white">
        Developed by @yecicen
      </footer>
    </div>
  )
}
