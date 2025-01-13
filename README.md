# IP Analyzer 🌐

A powerful Python-based tool designed for comprehensive IP address analysis, providing detailed insights into IP addresses, their geolocation, network characteristics, and security implications. Perfect for network administrators, security professionals, and developers who need detailed IP intelligence.

## 🛠️ Prerequisites

- Python 3.8 or higher
- macOS (for these specific instructions)
- pip (Python package installer)
- Minimum 2GB RAM
- Internet connection for real-time IP lookups

## 🎯 Key Features

### IP Analysis
- Comprehensive IP address validation
- IPv4 and IPv6 support
- CIDR notation parsing
- Subnet calculation
- Private/Public IP detection

### Geolocation Services
- Country and city detection
- ISP identification
- Timezone information
- Latitude and longitude coordinates
- Region and postal code data

### Network Intelligence
- ASN (Autonomous System Number) lookup
- Network range detection
- Reverse DNS lookup
- Connection type identification
- Network speed analysis

### Security Assessment
- Threat intelligence integration
- Blacklist checking
- VPN/Proxy detection
- TOR exit node verification
- Abuse history reporting

### Reporting
- JSON/CSV export capabilities
- Customizable report formats
- Batch processing support
- Historical data tracking
- Real-time monitoring

## 🚀 Setup Instructions

### Setting up Virtual Environment on macOS

1. Open Terminal and navigate to the project directory:
```bash
cd /path/to/ip_analyzer
```

2. Install virtualenv if you haven't already:
```bash
pip3 install virtualenv
```

3. Create a new virtual environment:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
```bash
source venv/bin/activate
```

💡 Pro Tip: Add this alias to your ~/.zshrc or ~/.bash_profile for quick activation:
```bash
alias ip-analyzer-activate="cd /path/to/ip_analyzer && source venv/bin/activate"
```

Note: To deactivate the virtual environment when you're done, simply run:
```bash
deactivate
```

### Installing Dependencies

With the virtual environment activated, you have two installation options:

1. Basic Installation (for users):
```bash
pip install -r requirements.txt
```

2. Development Installation (for contributors):
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Additional development tools
```

#### Dependencies Overview

The project uses the following major dependency categories:

1. **Core Dependencies**
   - requests>=2.31.0 - HTTP requests handling
   - ipaddress>=1.0.23 - IP address manipulation
   - python-dotenv>=1.0.0 - Environment management
   - pyyaml>=6.0.1 - Configuration handling

2. **IP Analysis & Networking**
   - netaddr>=0.8.0 - Network address manipulation
   - dnspython>=2.4.2 - DNS toolkit
   - geoip2>=4.7.0 - IP geolocation
   - maxminddb>=2.4.0 - MaxMind GeoIP database

3. **Data Processing**
   - pandas>=2.1.0 - Data analysis
   - numpy>=1.24.0 - Numerical operations
   - validators>=0.22.0 - Data validation

4. **Security Tools**
   - requests-ip-rotator>=1.0.14
   - pysafebrowsing>=0.1.2
   - tor-ip-api>=0.1.1

5. **Development Tools**
   - pytest>=7.4.2 - Testing
   - black>=23.7.0 - Code formatting
   - flake8>=6.1.0 - Linting
   - mypy>=1.5.1 - Type checking

💡 **Note**: Make sure your Python version is compatible (3.8 or higher) before installing dependencies.

### Configuration Setup

1. Copy the example configuration file:
```bash
cp config.example.yml config.yml
```

2. Edit the configuration file with your preferred settings:
```bash
nano config.yml
```

## 🏃‍♂️ Running the Application

1. Ensure your virtual environment is activated
2. Basic usage:
```bash
python analyze_ips.py <ip_address>
```

### Advanced Usage Examples

Single IP analysis:
```bash
python analyze_ips.py 8.8.8.8 --detailed
```

Batch processing:
```bash
python analyze_ips.py --input ips.txt --output report.json
```

Continuous monitoring:
```bash
python analyze_ips.py --monitor 192.168.1.1 --interval 60
```

## 📚 Project Structure

```
ip_analyzer/
├── README.md
├── requirements.txt
├── analyze_ips.py
├── config/
│   ├── config.yml
│   └── config.example.yml
├── src/
│   ├── analyzers/
│   ├── utils/
│   └── reports/
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   └── api.md
└── venv/
```

## 🔧 Troubleshooting

Common issues and solutions:

1. **API Rate Limiting**
   - Increase delay between requests
   - Use API key rotation

2. **SSL Certificate Issues**
   ```bash
   pip install --upgrade certifi
   ```

3. **Memory Usage**
   - Use batch processing for large datasets
   - Enable pagination for large reports

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Create a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8
```

## 📈 Performance Optimization

- Use async operations for batch processing
- Enable caching for frequent lookups
- Implement connection pooling
- Use bulk API requests when possible

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments

- MaxMind for GeoIP data
- AbuseIPDB for threat intelligence
- Contributors and maintainers
- Open-source community
