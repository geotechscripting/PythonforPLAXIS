import Link from "next/link";

const navItems = [
  { label: "Home", href: "/" },
  { label: "About the Book", href: "#about" },
  { label: "Examples", href: "#examples" },
  { label: "Resources", href: "#resources" },
  { label: "Contact", href: "#contact" },
];

function PythonLogo({ className }: { className?: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 110 110"
      className={className}
      aria-label="Python logo"
    >
      <defs>
        <linearGradient id="pyBlue" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#5A9FD4" />
          <stop offset="100%" stopColor="#306998" />
        </linearGradient>
        <linearGradient id="pyYellow" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#FFD43B" />
          <stop offset="100%" stopColor="#FFE873" />
        </linearGradient>
      </defs>
      <path
        d="M54.9 3.3c-26.1 0-24.5 11.3-24.5 11.3l.03 11.7h24.9v3.5H21.6S3.3 27.5 3.3 54.1s16 25.7 16 25.7h9.5V67.9s-.5-16 15.8-16h27.1s15.2.2 15.2-14.7V16.4S89.6 3.3 54.9 3.3zM40.1 11.3a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8z"
        fill="url(#pyBlue)"
      />
      <path
        d="M55.1 106.7c26.1 0 24.5-11.3 24.5-11.3l-.03-11.7H54.6v-3.5h33.7s18.3 2.3 18.3-24.3-16-25.7-16-25.7h-9.5v11.9s.5 16-15.8 16H38.2s-15.2-.2-15.2 14.7v20.8s-2.7 13.1 32 13.1zm14.8-8a4.9 4.9 0 1 1 0-9.8 4.9 4.9 0 0 1 0 9.8z"
        fill="url(#pyYellow)"
      />
    </svg>
  );
}

function PlaxisLogo({ className }: { className?: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 120 120"
      className={className}
      aria-label="PLAXIS — finite element mesh"
    >
      {/* Stylized FEM mesh triangle grid */}
      <defs>
        <linearGradient id="meshGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#00B4D8" />
          <stop offset="100%" stopColor="#0077B6" />
        </linearGradient>
      </defs>
      <g stroke="url(#meshGrad)" strokeWidth="1.5" fill="none" opacity="0.9">
        {/* Row 1 */}
        <polygon points="60,10 40,38 80,38" />
        {/* Row 2 */}
        <polygon points="40,38 20,66 60,66" />
        <polygon points="80,38 60,66 40,38" />
        <polygon points="80,38 60,66 100,66" />
        {/* Row 3 */}
        <polygon points="20,66 0,94 40,94" />
        <polygon points="60,66 40,94 20,66" />
        <polygon points="60,66 40,94 80,94" />
        <polygon points="100,66 80,94 60,66" />
        <polygon points="100,66 80,94 120,94" />
      </g>
      {/* Nodes */}
      <g fill="url(#meshGrad)">
        <circle cx="60" cy="10" r="3" />
        <circle cx="40" cy="38" r="3" />
        <circle cx="80" cy="38" r="3" />
        <circle cx="20" cy="66" r="3" />
        <circle cx="60" cy="66" r="3" />
        <circle cx="100" cy="66" r="3" />
        <circle cx="0" cy="94" r="3" />
        <circle cx="40" cy="94" r="3" />
        <circle cx="80" cy="94" r="3" />
        <circle cx="120" cy="94" r="3" />
      </g>
      {/* PLAXIS text */}
      <text
        x="60"
        y="114"
        textAnchor="middle"
        fill="#0077B6"
        fontSize="14"
        fontWeight="bold"
        fontFamily="sans-serif"
      >
        PLAXIS
      </text>
    </svg>
  );
}

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Navigation */}
      <nav className="border-b border-slate-700/50 backdrop-blur-sm bg-slate-900/80 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <span className="text-sm font-mono font-semibold text-amber-400 tracking-wide">
            PythonforPLAXIS
          </span>
          <ul className="hidden md:flex items-center gap-8">
            {navItems.map((item) => (
              <li key={item.label}>
                <Link
                  href={item.href}
                  className="text-sm text-slate-400 hover:text-white transition-colors"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
          <a
            href="https://github.com/geotechscripting/PythonforPLAXIS"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-slate-400 hover:text-white transition-colors"
          >
            GitHub
          </a>
        </div>
      </nav>

      {/* Hero */}
      <main className="flex-1 flex flex-col items-center justify-center px-6">
        <div className="max-w-3xl mx-auto text-center space-y-8 -mt-16">
          {/* Logos */}
          <div className="flex items-center justify-center gap-6">
            <PythonLogo className="h-20 w-20 sm:h-24 sm:w-24" />
            <span className="text-3xl text-slate-600 font-light select-none">
              +
            </span>
            <PlaxisLogo className="h-20 w-20 sm:h-24 sm:w-24" />
          </div>

          {/* Construction badge */}
          <div className="inline-flex items-center gap-2 rounded-full border border-amber-500/30 bg-amber-500/10 px-4 py-1.5">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-amber-400"></span>
            </span>
            <span className="text-xs font-medium text-amber-300 tracking-wide uppercase">
              Under Construction
            </span>
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-tight">
            Python Scripting
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-500">
              in PLAXIS
            </span>
          </h1>

          <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
            Automating Geotechnical Analysis and Modelling Workflows
          </p>

          <div className="w-16 h-px bg-gradient-to-r from-transparent via-slate-600 to-transparent mx-auto"></div>

          <p className="text-sm text-slate-500 max-w-lg mx-auto">
            Companion website for the book. Code examples, resources, and
            documentation coming soon.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <a
              href="https://github.com/geotechscripting/PythonforPLAXIS"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg bg-white text-slate-900 px-6 py-3 text-sm font-semibold hover:bg-slate-200 transition-colors"
            >
              View on GitHub
            </a>
            <span className="rounded-lg border border-slate-700 px-6 py-3 text-sm text-slate-500 cursor-default">
              Book &mdash; Coming Soon
            </span>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-6 px-6 text-center space-y-2">
        <p className="text-xs text-slate-600">
          &copy; {new Date().getFullYear()} geotechscripting
        </p>
        <p className="text-[10px] text-slate-700 max-w-xl mx-auto leading-relaxed">
          Python and the Python logo are trademarks of the Python Software
          Foundation. PLAXIS is a registered trademark of Bentley Systems,
          Incorporated. This website is not affiliated with or endorsed by the
          Python Software Foundation or Bentley Systems.
        </p>
      </footer>
    </div>
  );
}
