import Head from 'next/head'
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';


export default function Home() {
  const data = [
    {
      "date": "14:30",
      "price": 37000,
      "predict": 38000,
      "source": "Nomics"
    },
    {
      "date": "14:35",
      "price": 35000,
      "predict": 34000,
      "source": "Nomics"
    },
    {
      "date": "14:40",
      "price": 36500,
      "predict": 37100,
      "source": "Nomics"
    },
    {
      "date": "14:45",
      "price": 36900,
      "predict": 38000,
      "source": "Nomics"
    },
    {
      "date": "14:50",
      "price": 36000,
      "predict": 37000,
      "source": "Nomics"
    },
    {
      "date": "14:55",
      "price": 37000,
      "predict": 38000,
      "source": "Nomics"
    },
    {
      "date": "15:00",
      "price": 35000,
      "predict": 34000,
      "source": "Nomics"
    },
    {
      "date": "15:05",
      "price": 36500,
      "predict": 37100,
      "source": "Nomics"
    },
    {
      "date": "15:10",
      "price": 36900,
      "predict": 38000,
      "source": "Nomics"
    },
    {
      "date": "15:15",
      "price": 36000,
      "predict": 37000,
      "source": "Nomics"
    },
  ]
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <Head>
        <title>Bitcoin Price Prediction</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1 className="h-20 mt-40 text-xl">Bitcoin Price Prediction using LSTM Model</h1>
      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
        
        <div>
        <LineChart width={800} height={300} data={data}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="5 5" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />
          <Line type="monotone" dataKey="predict" stroke="#82ca9d" />
          <Line type="monotone" dataKey="source" stroke="red" />
        </LineChart>
        </div>
        
      </main>
      
      <footer className="flex items-center justify-center w-full h-24 border-t">
        Developed by @yecicen
      </footer>
    </div>
  )
}
