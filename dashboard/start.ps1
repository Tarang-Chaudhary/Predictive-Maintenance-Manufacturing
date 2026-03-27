# Start Predictive Analytics Dashboard

Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoProfile -Command cd backend; python main.py" -WindowStyle Normal

Write-Host "Starting Frontend (Vite)..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoProfile -Command cd frontend; npm run dev" -WindowStyle Normal

Write-Host "Dashboard is launching!" -ForegroundColor Yellow
Write-Host "Backend: http://localhost:8000"
Write-Host "Frontend: http://localhost:5173"
