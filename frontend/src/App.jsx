import { useState } from 'react'
import './App.css'


export default function App() {
  const [city, setCity] = useState('João Monlevade, Brazil')
  const [distance, setDistance] = useState(50)

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('City:', city)
    console.log('Distance:', distance)
    // Chamar a API do backend
  }

  return (
    <div className="min-h-screen bg-gray-100 p-4">
    <header className='mb-6'>
      <h1 className='text-3xl font-bold text-center text-blue-800'>
        Cobertura Inteligente de Cidades com Wi-Fi
      </h1>
      </header>

      <main className='max-w-md mx-auto bg-white p-6 rounded-lg shadow-md'>
        <form  onSubmit={handleSubmit} className='space-y-4'>
          <div>
            <label className='block font-semibold text-black mb-1'>City</label>
            <input 
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            className='w-full border px-3 py-2 rounded-md text-gray-900 bg-white'
            placeholder='Ex: Belo Horizonte, Brazil'
            />
          </div>

          <div>
            <label className='block font-semibold mb-1'>Distância máxima entre conexões (metros)</label>
            <input 
            type="number"
            value={distance}
            onChange={(e) => setDistance(Number(e.target.value))}
            className='w-full border px-3 py-2 rounded-md text-gray-900 bg-white'
            min={10}
            max={500}
            />
          </div>

          <button
            type="submit"
            className='bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded'
          >
            Gerar cobertura
          </button>
        </form>
      </main>
    </div>

  )
}


