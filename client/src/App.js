import React, {useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState ([{}])
  
  let url = window.location.pathname


  useEffect(() => {
    fetch(url).then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div className="App">
          <h1>Please select a user by their number in the format: http://localhost/user/7/</h1>
          <h2>User ID: {data.id}</h2>
          <h2>Email: {data.email}</h2>
          <h2>First Name: {data.first_name}</h2>
          <h2>Last Name: {data.last_name}</h2>
          <img src= {data.avatar} alt="Avatar Missing" width="256" height="256"></img>

    </div>
  );
}

export default App;
