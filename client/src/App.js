import './App.css';
import { React, useEffect, useState } from 'react';
import { FormControl, InputLabel, MenuItem, Select, Card, Grid } from '@mui/material';

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState("");
  const [repos, setRepos] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/v1/users")
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw res;
        }
      })
      .then(data => {
        data.users.unshift("Select a user");
        setUsers(data.users);
        setSelectedUser("Select a user");
      })
      .catch(
        console.log("Error occurred")
      );
  }, []);


  useEffect(() => {
    fetch(`http://localhost:8000/v1/repos?username=${selectedUser}`)
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw res;
        }
      })
      .then(data => {
        setRepos(data.repositories);
      })
      .catch(
        console.log("Error occurred")
      );
  }, [selectedUser]);



  const handleChange = (e) => {
    setSelectedUser(e.target.value);
  };


  const userSelect = users.map((user, i) => {
    return (
      <MenuItem value={user}>{user}</MenuItem>
    )
  }
  );


  const repoList = repos.map((repo, i) => {
    return (
      <Card variant="outlined" className='Repo-card' key={i}>{repo}</Card>
    )
  }
  );

  return (
    <div className="App">
      <header className="App-header">
        <h1>Github Profiles</h1>
      </header>
      <section className='App-body'>
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">User</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={selectedUser}
            label="Age"
            onChange={(e) => handleChange(e)}
          >
            {userSelect}
          </Select>
        </FormControl>
      </section>
      <section className='Repo-section'>
        <h2>Repositories</h2>
        {repos.length !== 0 ? <Grid container rowSpacing={{ xs: 1, sm: 2, md: 3 }} columnSpacing={{ xs: 1, sm: 2, md: 3 }} style={{ marginLeft: '10px' }}>{repoList}</Grid> : <div> No Repositories</div>}
      </section>
    </div>
  );
}

export default App;
