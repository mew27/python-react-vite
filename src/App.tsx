import { useState } from 'react'
import reactLogo from './assets/react.svg'
import pythonLogo from './assets/python.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Ticker } from './Ticker/Ticker'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
        <a href="https://python.org" target="_blank">
          <img src={pythonLogo} className="logo" alt="Python logo" />
        </a>
      </div>
      <h1>Vite + React + Python</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR. Hot module reload rules
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite, React and Python logos to learn more
      </p>
      <Ticker></Ticker>
    </>
  )
}

export default App
