// Inside /src/store/systemsSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async thunk for fetching all systems
export const fetchSystems = createAsyncThunk(
  'systems/fetchSystems',
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch('/api/systems');
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      return data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Async thunk for fetching a single system by ID
export const fetchSystemById = createAsyncThunk(
  'systems/fetchSystemById',
  async (systemId, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/systems/${systemId}`);
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      return data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const systemsSlice = createSlice({
  name: 'systems',
  initialState: {
    systems: [],
    currentSystem: null,
    status: 'idle',
    error: null,
  },
  reducers: {
    // Reducers can be added here if needed
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchSystems.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchSystems.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.systems = action.payload;
      })
      .addCase(fetchSystems.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      })
      .addCase(fetchSystemById.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchSystemById.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.currentSystem = action.payload;
      })
      .addCase(fetchSystemById.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      });
  },
});

export default systemsSlice.reducer;
