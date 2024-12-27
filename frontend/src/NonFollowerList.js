import React, { useState, useEffect } from 'react';
import { fetchNonFollowers } from './api';

function NonFollowerList() {
    const [nonFollowers, setNonFollowers] = useState([]);
    const [selected, setSelected] = useState([]);
    const [filePath, setFilePath] = useState('');

    useEffect(() => {
        const loadNonFollowers = async () => {
            const response = await fetchNonFollowers();
            setNonFollowers(response.data.non_followers);
            setFilePath(response.data.file_path);
        };
        loadNonFollowers();
    }, []);

    const handleSelect = (username) => {
        setSelected(prev => prev.includes(username) 
            ? prev.filter(u => u !== username) 
            : [...prev, username]);
    };

    return (
        <div>
            <h2>Non-Followers</h2>
            {nonFollowers.map(user => (
                <div key={user.username}>
                    <input 
                        type="checkbox" 
                        onChange={() => handleSelect(user.username)} 
                    />
                    {user.full_name} (@{user.username})
                </div>
            ))}
            <button onClick={() => window.location.href = `/confirm?file=${filePath}`}>
                Proceed to Unfollow
            </button>
        </div>
    );
}

export default NonFollowerList;
