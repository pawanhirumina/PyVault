## PyVault

A lightweight, CLI-based password manager inspired by Bitwarden.
Built for personal use — secure, simple, and fully under your control. Clone it, connect your own database, and own your vault.

### Features

* **Secure Vault:** Encrypted password storage using your own Supabase backend
* **CLI First:** Fast, minimal, and keyboard-friendly
* **Self-Hosted:** You own your data. No third-party cloud
* **Authentication:** Secure authentication via Supabase

### Tech Stack

* Python
* Supabase (Database & Auth)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/pawanhirumina/PyVault
cd PyVault
```

**2. Configure Environment Variables**

PyVault reads Supabase credentials from:

```bash
~/.config/pyvault/supabase.env
```

Create the directory:

```bash
mkdir -p ~/.config/pyvault
```

Create the environment file:

```bash
nano ~/.config/pyvault/supabase.env
```

Add your Supabase credentials:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the virtual environment**

On macOS / Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

To exit the environment:

```bash
deactivate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run PyVault**

```bash
python main.py
```

### Configuration

PyVault keeps sensitive configuration files outside the project directory:

```
~/.config/
└── pyvault/
    └── supabase.env
```

This prevents accidentally committing credentials to GitHub.

### Future Enhancements

* [ ] Local secure storage for Supabase environment variables
* [ ] Encrypted local cache for offline access
* [ ] Password generator and strength checker
* [ ] Import / Export vault functionality
* [ ] Publish as a pip package (`pip install pyvault`)

### Contributing

This is a personal project, but suggestions and pull requests are welcome.

### License

MIT License — feel free to use it for your own setup.
