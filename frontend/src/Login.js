import React, { useState } from 'react';
import { login } from './api';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        try {
            await login(username, password);
            alert('Login successful!');
        } catch (error) {
            alert('Login failed: ' + error.response.data.detail);
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input placeholder="Password" type="password" onChange={e => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;
