# Smart Shipyard Ontology System

A comprehensive ontology-based system for managing smart shipyard operations, integrating IoT sensors, manufacturing processes, ship components, workforce management, and digital twin technology for Industry 4.0 shipyards.

## 🚢 Overview

The Smart Shipyard Ontology System provides a semantic framework for modeling and managing all aspects of modern shipyard operations. It enables intelligent data integration, automated reasoning, and knowledge-based decision-making for shipyard management.

## ✨ Key Features

- **Vessel Management**: Track ship construction and maintenance with detailed component hierarchies
- **IoT Sensor Network**: Integrate temperature, vibration, pressure, humidity, position, and safety sensors
- **Workforce Management**: Manage workers, engineers, inspectors, and their skills and certifications
- **Manufacturing Processes**: Monitor welding, assembly, painting, inspection, and maintenance operations
- **Equipment Tracking**: Real-time status of cranes, robots, cutting machines, and transport vehicles
- **Material Inventory**: Track steel plates, paint, welding rods, electrical cables, and other materials
- **Digital Systems Integration**: Support for MES, ERP, Digital Twin, and AI/ML systems
- **Quality Control**: Comprehensive inspection and quality assurance workflows
- **Safety Monitoring**: Built-in safety sensors and safety officer tracking
- **Analytics & KPIs**: Generate insights on vessel completion, workforce utilization, and more

## 📋 Requirements

- Python >= 3.13.1
- owlready2 >= 0.48

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/bedro96/smartshipyard.git
cd smartshipyard
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install owlready2
```

## 🚀 Usage

### Running the Ontology System

Execute the main ontology script to create and populate the smart shipyard ontology:

```bash
python ontology.py
```

This will:
1. Create the ontology structure with all classes and properties
2. Populate it with sample data (vessels, workers, sensors, processes, etc.)
3. Execute various queries to demonstrate the system capabilities
4. Generate analytics and KPIs
5. Save the ontology to `smart_shipyard.owl`

### Running the Basic Application

```bash
python main.py
```

## 🏗️ Ontology Structure

The ontology is organized into the following main categories:

### Physical Infrastructure
- **PhysicalAsset**: Base class for all physical assets
  - **Vessel**: Ships under construction or maintenance
    - **VesselComponent**: Hull, Engine, NavigationSystem, ElectricalSystem
  - **ShipyardFacility**: DryDock, Workshop (Welding, Painting, Assembly), Warehouse

### Equipment & Machinery
- **Equipment**: Crane, WeldingRobot, CuttingMachine, TransportVehicle

### IoT & Sensors
- **Sensor**: TemperatureSensor, VibrationSensor, PressureSensor, HumiditySensor, PositionSensor, SafetySensor, QualitySensor

### Human Resources
- **Person**: Worker (Welder, Electrician, Painter), Engineer, QualityInspector, SafetyOfficer, Manager

### Processes & Operations
- **Process**: WeldingProcess, AssemblyProcess, InspectionProcess, PaintingProcess, MaintenanceProcess

### Materials & Inventory
- **Material**: SteelPlate, Paint, WeldingRod, ElectricalCable

### Digital Systems
- **DigitalSystem**: MES, ERP, DigitalTwin, AISystem

### Object Properties (Relationships)
- `locatedIn`: Physical location relationships
- `partOf`: Component relationships
- `installedOn`: Sensor installation
- `operatedBy`: Equipment operation by workers
- `supervisedBy`: Supervision relationships
- `inspectedBy`: Quality inspection
- `monitors`: Sensor monitoring
- `usedIn`: Material usage in processes
- `produces`: Process outputs
- `requires`: Process requirements
- `manages`: Digital system management

### Data Properties (Attributes)
- Identity: `hasName`, `hasID`, `hasStatus`, `locatedAt`
- Capacity: `hasCapacity`, `hasQuantity`
- Sensor readings: `hasTemperature`, `hasVibration`, `hasPressure`, `hasHumidity`, `hasCoordinates`
- Progress: `hasCompletionPercentage`
- Vessel specs: `hasVesselType`, `hasLength`, `hasDeadweight`
- Worker info: `hasExperience`, `hasCertification`

## 🌐 Visualize the Ontology

You can visualize the `smart_shipyard.owl` file online using WebVOWL:

👉 **[WebVOWL - Visual Ontology Viewer](https://service.tib.eu/webvowl/)**

Simply upload the `smart_shipyard.owl` file to explore the ontology structure interactively with a visual graph representation showing all classes, properties, and their relationships.

## 📊 Example Queries

The system supports various queries including:

- Find all vessels and their completion status
- List workforce by role and experience
- Monitor IoT sensor readings
- Track active manufacturing processes
- Check equipment operational status
- View material inventory levels
- Analyze digital systems integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available for educational and research purposes.

## 🔗 Repository

[https://github.com/bedro96/smartshipyard](https://github.com/bedro96/smartshipyard)

---

**Built for Smart Manufacturing and Industry 4.0 Shipyard Operations**
