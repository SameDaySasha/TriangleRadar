// Inside /src/store/systemsSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async thunk for fetching systems
export const fetchSystems = createAsyncThunk(
  'systems/fetchSystems',
  async (_, { rejectWithValue }) => {
    try {
      // Ensure the fetch URL is correctly formatted
      const response = await fetch('/api/systems');
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
        // Add fetched systems to the array
        state.systems = action.payload;
      })
      .addCase(fetchSystems.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload;
      });
  },
});

export default systemsSlice.reducer;
