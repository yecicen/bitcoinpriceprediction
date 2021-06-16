import Head from 'next/head'
import { ResponsiveContainer, LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';


export default function Home() {
  const data = [
    {
      "date": "21:30",
      "price": 36357,
      "predict": 36552,
      "source": "Nomics"
    },
    {
      "date": "21:35",
      "price": 36705,
      "predict": 36395,
      "source": "Nomics"
    },
    {
      "date": "21:40",
      "price": 36716,
      "predict": 36685,
      "source": "Nomics"
    },
    {
      "date": "21:45",
      "price": 36900,
      "predict": 37110,
      "source": "Nomics"
    },
    {
      "date": "21:50",
      "price": 37213,
      "predict": 37517,
      "source": "Nomics"
    },
    {
      "date": "21:55",
      "price": 37367,
      "predict": 38000,
      "source": "Nomics"
    },
    {
      "date": "22:00",
      "price": 37471,
      "predict": 37349,
      "source": "Nomics"
    },
    {
      "date": "22:05",
      "price": 37294,
      "predict": 37437,
      "source": "Nomics"
    },
    {
      "date": "22:10",
      "price": 37146,
      "predict": 37117,
      "source": "Nomics"
    },
    {
      "date": "22:15",
      "price": 36986,
      "predict": 37096,
      "source": "Nomics"
    },
  ]
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-gray-900">
      <Head>
        <title>Bitcoin Price Prediction</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <h1 className="h-20 text-xl text-white text-center">Bitcoin Price Prediction using LSTM Model</h1>
      <main className="flex flex-col items-center justify-center w-full px-5 md:px-20 flex-1 text-center">

          <ResponsiveContainer height={500}>
            <LineChart data={data} className="bg-gray-800"
              margin={{ top: 20, right: 10, left: 5, bottom: 10 }}>
              <CartesianGrid strokeDasharray="5 5" />
              <XAxis dataKey="date" />
              <YAxis domain={['dataMin', 'dataMax']} />
              <Tooltip />
              <Line type="monotone" dataKey="price" stroke="#8884d8" />
              <Line type="basis" dataKey="predict" stroke="#82ca9d" />
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
