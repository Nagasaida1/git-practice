export default function Widget() {
    return (
        <div className="bg-[var(--background)] text-[var(--foreground)] p-4">
          
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <img src="https://placehold.co/32x32" alt="Microsoft Start Logo" className="h-8 w-8">
              <span className="text-xl font-semibold">Microsoft Start</span>
            </div>
            <div className="flex items-center space-x-2">
              <input type="text" placeholder="Search the web" className="border-[var(--border)] rounded-full px-4 py-2">
              <img src="https://placehold.co/32x32" alt="User Profile" className="h-8 w-8 rounded-full">
            </div>
          </div>
          
          <div className="flex space-x-2 mb-4">
            <button className="bg-[var(--primary)] text-[var(--primary-foreground)] px-4 py-2 rounded-full">Discover</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Following</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">News</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Sports</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Play</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Money</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Gaming</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Shopping</button>
            <button className="bg-[var(--secondary)] text-[var(--secondary-foreground)] px-4 py-2 rounded-full">Health</button>
          </div>
          
          <div className="grid grid-cols-3 gap-4">
            
            <div className="col-span-2">
              <div className="relative">
                <img src="https://placehold.co/600x300" alt="Ad Image" className="w-full h-auto rounded-lg">
                <div className="absolute bottom-0 left-0 p-4 bg-black bg-opacity-50 text-white rounded-b-lg">
                  <p className="text-sm">Max Life Savings Plan</p>
                  <p className="text-lg font-bold">Rs. 2,500/month invested starting 2004, you'd have got Rs. 1.02 crores today! *T&C apply</p>
                </div>
              </div>
            </div>
        
        <div className="col-span-1">
          <div className="bg-[var(--card)] text-[var(--card-foreground)] p-4 rounded-lg">
            <div className="flex items-center justify-between">
              <p className="font-semibold">ICC</p>
              <img src="https://placehold.co/24x24" alt="Settings Icon" className="h-6 w-6">
            </div>
            <div className="flex items-center justify-between mt-2">
              <div className="text-center">
                <p className="text-lg font-bold">ENG</p>
                <p>416</p>
              </div>
              <div className="text-center">
                <p className="text-lg font-bold">WI</p>
                <p>457</p>
              </div>
            </div>
            <p className="text-center mt-2">ENG lead by 326 runs</p>
            <p className="text-center mt-2">25 Jul, 3:30 pm</p>
            <p className="text-center mt-2">CWI Service Cricket Club, Stormont</p>
            <div className="flex justify-center mt-4">
              <button className="bg-[var(--primary)] text-[var(--primary-foreground)] px-4 py-2 rounded-full">Follow</button>
              <button className="bg-[var(--destructive)] text-[var(--destructive-foreground)] px-4 py-2 rounded-full ml-2">No thanks</button>
            </div>
          </div>
        </div>
          </div>
        </div>
    )
}