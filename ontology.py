"""
Smart Shipyard Ontology System
A comprehensive ontology for managing smart shipyard operations including
IoT sensors, manufacturing processes, ship components, and workforce management.

Install: pip install owlready2 rdflib
"""

from owlready2 import *
from datetime import datetime
import random


# ============================================================================
# SMART SHIPYARD ONTOLOGY CREATION
# ============================================================================

def create_smart_shipyard_ontology():
    """Create a comprehensive smart shipyard ontology."""
    
    print("\n" + "="*80)
    print("CREATING SMART SHIPYARD ONTOLOGY")
    print("="*80)
    
    # Create ontology
    onto = get_ontology("http://example.org/smartshipyard.owl")
    
    with onto:
        # ====================================================================
        # MAIN CLASSES - Physical Infrastructure
        # ====================================================================
        
        class PhysicalAsset(Thing):
            """Base class for all physical assets in the shipyard"""
            pass
        
        class Vessel(PhysicalAsset):
            """Ships being constructed or maintained"""
            pass
        
        class VesselComponent(PhysicalAsset):
            """Components that make up a vessel"""
            pass
        
        class Hull(VesselComponent):
            """Ship hull structure"""
            pass
        
        class Engine(VesselComponent):
            """Propulsion system"""
            pass
        
        class NavigationSystem(VesselComponent):
            """Navigation and control systems"""
            pass
        
        class ElectricalSystem(VesselComponent):
            """Electrical infrastructure"""
            pass
        
        class ShipyardFacility(PhysicalAsset):
            """Physical facilities in the shipyard"""
            pass
        
        class DryDock(ShipyardFacility):
            """Dry dock for ship construction/maintenance"""
            pass
        
        class Workshop(ShipyardFacility):
            """Manufacturing and assembly workshop"""
            pass
        
        class WeldingStation(Workshop):
            """Station for welding operations"""
            pass
        
        class PaintingStation(Workshop):
            """Station for painting and coating"""
            pass
        
        class AssemblyStation(Workshop):
            """Station for component assembly"""
            pass
        
        class Warehouse(ShipyardFacility):
            """Storage facility for materials and components"""
            pass
        
        # ====================================================================
        # EQUIPMENT AND MACHINERY
        # ====================================================================
        
        class Equipment(Thing):
            """Manufacturing and construction equipment"""
            pass
        
        class Crane(Equipment):
            """Heavy lifting equipment"""
            pass
        
        class WeldingRobot(Equipment):
            """Automated welding system"""
            pass
        
        class CuttingMachine(Equipment):
            """Metal cutting equipment"""
            pass
        
        class TransportVehicle(Equipment):
            """Material transport vehicles"""
            pass
        
        # ====================================================================
        # IoT AND SENSORS
        # ====================================================================
        
        class Sensor(Thing):
            """IoT sensors for monitoring"""
            pass
        
        class TemperatureSensor(Sensor):
            """Temperature monitoring"""
            pass
        
        class VibrationSensor(Sensor):
            """Vibration monitoring"""
            pass
        
        class PressureSensor(Sensor):
            """Pressure monitoring"""
            pass
        
        class HumiditySensor(Sensor):
            """Humidity monitoring"""
            pass
        
        class PositionSensor(Sensor):
            """GPS/location tracking"""
            pass
        
        class SafetySensor(Sensor):
            """Safety monitoring (gas, fire, etc.)"""
            pass
        
        class QualitySensor(Sensor):
            """Quality inspection sensors"""
            pass
        
        # ====================================================================
        # HUMAN RESOURCES
        # ====================================================================
        
        class Person(Thing):
            """Human resources"""
            pass
        
        class Worker(Person):
            """Shipyard worker"""
            pass
        
        class Welder(Worker):
            """Welding specialist"""
            pass
        
        class Electrician(Worker):
            """Electrical systems specialist"""
            pass
        
        class Painter(Worker):
            """Painting specialist"""
            pass
        
        class Engineer(Person):
            """Engineering staff"""
            pass
        
        class QualityInspector(Person):
            """Quality control inspector"""
            pass
        
        class SafetyOfficer(Person):
            """Safety management"""
            pass
        
        class Manager(Person):
            """Management staff"""
            pass
        
        # ====================================================================
        # PROCESSES AND OPERATIONS
        # ====================================================================
        
        class Process(Thing):
            """Manufacturing and construction processes"""
            pass
        
        class WeldingProcess(Process):
            """Welding operations"""
            pass
        
        class AssemblyProcess(Process):
            """Component assembly"""
            pass
        
        class InspectionProcess(Process):
            """Quality inspection"""
            pass
        
        class PaintingProcess(Process):
            """Surface treatment and painting"""
            pass
        
        class MaintenanceProcess(Process):
            """Equipment maintenance"""
            pass
        
        # ====================================================================
        # MATERIALS AND INVENTORY
        # ====================================================================
        
        class Material(Thing):
            """Raw materials and supplies"""
            pass
        
        class SteelPlate(Material):
            """Steel plates for hull construction"""
            pass
        
        class Paint(Material):
            """Coating materials"""
            pass
        
        class WeldingRod(Material):
            """Welding consumables"""
            pass
        
        class ElectricalCable(Material):
            """Electrical wiring"""
            pass
        
        # ====================================================================
        # DIGITAL SYSTEMS
        # ====================================================================
        
        class DigitalSystem(Thing):
            """Digital infrastructure and software"""
            pass
        
        class MES(DigitalSystem):
            """Manufacturing Execution System"""
            pass
        
        class ERP(DigitalSystem):
            """Enterprise Resource Planning"""
            pass
        
        class DigitalTwin(DigitalSystem):
            """Digital twin representation"""
            pass
        
        class AISystem(DigitalSystem):
            """AI/ML system for optimization"""
            pass
        
        # ====================================================================
        # OBJECT PROPERTIES (RELATIONSHIPS)
        # ====================================================================
        
        class locatedIn(ObjectProperty):
            """Physical location relationship"""
            domain = [PhysicalAsset | Equipment | Person]
            range = [ShipyardFacility]
        
        class partOf(ObjectProperty):
            """Component relationship"""
            domain = [VesselComponent]
            range = [Vessel]
        
        class installedOn(ObjectProperty, FunctionalProperty):
            """Sensor installation"""
            domain = [Sensor]
            range = [PhysicalAsset | Equipment]
        
        class operatedBy(ObjectProperty, FunctionalProperty):
            """Equipment operation"""
            domain = [Equipment | Process]
            range = [Worker]
        
        class supervisedBy(ObjectProperty, FunctionalProperty):
            """Supervision relationship"""
            domain = [Worker | Process]
            range = [Manager | Engineer]
        
        class inspectedBy(ObjectProperty, FunctionalProperty):
            """Inspection relationship"""
            domain = [Vessel | VesselComponent | Process]
            range = [QualityInspector]
        
        class monitors(ObjectProperty, FunctionalProperty):
            """Monitoring relationship"""
            domain = [Sensor]
            range = [PhysicalAsset | Equipment | Process]
        
        class usedIn(ObjectProperty, FunctionalProperty):
            """Material usage"""
            domain = [Material]
            range = [Process]
        
        class produces(ObjectProperty, FunctionalProperty):
            """Production relationship"""
            domain = [Process]
            range = [VesselComponent | Vessel]
        
        class requires(ObjectProperty, FunctionalProperty):
            """Dependency relationship"""
            domain = [Process]
            range = [Equipment | Material | Worker]
        
        class manages(ObjectProperty):
            """Management relationship"""
            domain = [DigitalSystem]
            range = [Process | Equipment | Material]
            
        class installedOn(ObjectProperty, FunctionalProperty):
            domain = [Sensor]
            range = [PhysicalAsset | Equipment | ShipyardFacility]
        
        # ====================================================================
        # DATA PROPERTIES (ATTRIBUTES)
        # ====================================================================
        
        class hasName(DataProperty, FunctionalProperty):
            domain = [Thing]
            range = [str]
        
        class hasID(DataProperty, FunctionalProperty):
            domain = [Thing]
            range = [str]
        
        class hasStatus(DataProperty, FunctionalProperty):
            """Operational status"""
            domain = [Equipment | Process | Vessel]
            range = [str]
        
        class locatedAt(DataProperty, FunctionalProperty):
            domain = [PhysicalAsset | Equipment | Sensor]
            range = [str]
        class hasCapacity(DataProperty, FunctionalProperty):
            """Capacity specification"""
            domain = [Equipment | ShipyardFacility]
            range = [float]
        
        class hasTemperature(DataProperty, FunctionalProperty):
            domain = [TemperatureSensor | Process]
            range = [float]
        
        class hasVibration(DataProperty, FunctionalProperty):
            domain = [VibrationSensor]
            range = [float]
        
        class hasPressure(DataProperty):
            domain = [PressureSensor]
            range = [float]
        
        class hasHumidity(DataProperty):
            domain = [HumiditySensor]
            range = [float]
        
        class hasCoordinates(DataProperty, FunctionalProperty):
            domain = [PositionSensor | ShipyardFacility]
            range = [str]
        
        class hasQuantity(DataProperty, FunctionalProperty):
            domain = [Material]
            range = [int]
        
        class hasCompletionPercentage(DataProperty, FunctionalProperty):
            domain = [Process | Vessel]
            range = [float]
        
        class hasVesselType(DataProperty, FunctionalProperty):
            domain = [Vessel]
            range = [str]
        
        class hasLength(DataProperty, FunctionalProperty):
            domain = [Vessel]
            range = [float]
        
        class hasDeadweight(DataProperty, FunctionalProperty):
            domain = [Vessel]
            range = [float]
        
        class hasExperience(DataProperty, FunctionalProperty):
            domain = [Worker]
            range = [int]
        
        class hasCertification(DataProperty):
            domain = [Worker]
            range = [str]
        
        class hasTimestamp(DataProperty, FunctionalProperty):
            domain = [Sensor | Process]
            range = [str]
        
        class hasPriority(DataProperty, FunctionalProperty):
            domain = [Process]
            range = [str]
        
        class hasQualityScore(DataProperty, FunctionalProperty):
            domain = [VesselComponent | Process]
            range = [float]
        
    print("✓ Ontology structure created")
    return onto


# ============================================================================
# POPULATE WITH SAMPLE DATA
# ============================================================================

def populate_shipyard_data(onto):
    """Populate the ontology with realistic shipyard data."""
    
    print("\nPopulating with sample data...")
    
    with onto:
        # ====================================================================
        # CREATE FACILITIES
        # ====================================================================
        
        drydock1 = onto.DryDock("DryDock_01")
        drydock1.hasName = "Main Dry Dock 1"
        drydock1.hasID = "DD-001"
        drydock1.hasCapacity = 150000.0  # tonnage
        
        drydock2 = onto.DryDock("DryDock_02")
        drydock2.hasName = "Dry Dock 2"
        drydock2.hasID = "DD-002"
        drydock2.hasCapacity = 100000.0  # tonnage
        
        welding_shop = onto.WeldingStation("WeldingShop_01")
        welding_shop.hasName = "Primary Welding Station"
        welding_shop.hasID = "WS-001"
        
        painting_shop = onto.PaintingStation("PaintingShop_01")
        painting_shop.hasName = "Coating and Painting Station"
        painting_shop.hasID = "PS-001"
        
        assembly_shop = onto.AssemblyStation("AssemblyShop_01")
        assembly_shop.hasName = "Main Assembly Station"
        assembly_shop.hasID = "AS-001"

        warehouse1 = onto.Warehouse("Warehouse_01")
        warehouse1.hasName = "Materials Warehouse"
        warehouse1.hasID = "WH-001"
        warehouse1.hasCapacity = 5000.0  # square meters
        
        # ====================================================================
        # CREATE VESSELS UNDER CONSTRUCTION
        # ====================================================================
        
        vessel1 = onto.Vessel("Vessel_Container_001")
        vessel1.hasName = "Container Ship Pacific Star"
        vessel1.hasID = "V-CS-001"
        vessel1.hasVesselType = "Container Ship"
        vessel1.hasLength = 350.0  # meters   
        vessel1.hasDeadweight = 145000.0  # tons
        vessel1.hasCompletionPercentage = 65.0
        vessel1.hasStatus = "Under Construction"
        vessel1.locatedAt = "drydock1"
        
        vessel2 = onto.Vessel("Vessel_Tanker_001")
        vessel2.hasName = "Oil Tanker Atlantic Pride"
        vessel2.hasID = "V-TK-001"
        vessel2.hasVesselType = "Oil Tanker"
        vessel2.hasLength = 280.0
        vessel2.hasDeadweight = 95000.0
        vessel2.hasCompletionPercentage = 40.0
        vessel2.hasStatus = "Under Construction"
        vessel2.locatedAt = "drydock2"
        
        # ====================================================================
        # CREATE VESSEL COMPONENTS
        # ====================================================================
        
        hull1 = onto.Hull("Hull_V001")
        hull1.hasName = "Hull - Pacific Star"
        hull1.hasID = "H-V001"
        hull1.partOf.append(vessel1)
        hull1.hasQualityScore = 95.5
        
        engine1 = onto.Engine("Engine_V001")
        engine1.hasName = "Main Engine - Pacific Star"
        engine1.hasID = "E-V001"
        engine1.partOf.append(vessel1)
        engine1.hasQualityScore = 98.0
        
        nav_system1 = onto.NavigationSystem("NavSystem_V001")
        nav_system1.hasName = "Navigation System - Pacific Star"
        nav_system1.hasID = "NS-V001"
        nav_system1.partOf.append(vessel1)
        
        electrical1 = onto.ElectricalSystem("ElecSystem_V001")
        electrical1.hasName = "Electrical System - Pacific Star"
        electrical1.hasID = "ES-V001"
        electrical1.partOf.append(vessel1)
        
        # ====================================================================
        # CREATE EQUIPMENT
        # ====================================================================
        
        crane1 = onto.Crane("Crane_001")
        crane1.hasName = "Gantry Crane 1"
        crane1.hasID = "CR-001"
        crane1.hasCapacity = 500.0  # tons
        crane1.hasStatus = "Operational"
        crane1.locatedAt = "drydock1"
        
        welding_robot1 = onto.WeldingRobot("WeldRobot_001")
        welding_robot1.hasName = "Automated Welding Robot 1"
        welding_robot1.hasID = "WR-001"
        welding_robot1.hasStatus = "Operational"
        welding_robot1.locatedAt = "welding_shop"
        
        cutting_machine1 = onto.CuttingMachine("CuttingMachine_001")
        cutting_machine1.hasName = "Plasma Cutting Machine"
        cutting_machine1.hasID = "CM-001"
        cutting_machine1.hasStatus = "Operational"
        cutting_machine1.locatedAt = "assembly_shop"
        
        # ====================================================================
        # CREATE IoT SENSORS
        # ====================================================================
        
        temp_sensor1 = onto.TemperatureSensor("TempSensor_WR001")
        temp_sensor1.hasName = "Temperature Sensor - Welding Robot 1"
        temp_sensor1.hasID = "TS-WR001"
        temp_sensor1.installedOn = welding_robot1
        temp_sensor1.monitors = welding_robot1
        temp_sensor1.hasTemperature = 45.5
        temp_sensor1.hasTimestamp = datetime.now().isoformat()
        
        vib_sensor1 = onto.VibrationSensor("VibSensor_CR001")
        vib_sensor1.hasName = "Vibration Sensor - Crane 1"
        vib_sensor1.hasID = "VS-CR001"
        vib_sensor1.installedOn = crane1
        vib_sensor1.monitors = crane1
        vib_sensor1.hasVibration = 2.3
        vib_sensor1.hasTimestamp = datetime.now().isoformat()
        
        pos_sensor1 = onto.PositionSensor("PosSensor_V001")
        pos_sensor1.hasName = "Position Tracker - Pacific Star"
        pos_sensor1.hasID = "PS-V001"
        pos_sensor1.installedOn = vessel1
        pos_sensor1.monitors = vessel1
        pos_sensor1.hasCoordinates = "37.8267° N, 122.4233° W"
        
        safety_sensor1 = onto.SafetySensor("SafetySensor_WS001")
        safety_sensor1.hasName = "Gas Detection - Welding Shop"
        safety_sensor1.hasID = "SS-WS001"
        safety_sensor1.installedOn = welding_shop
        safety_sensor1.monitors = welding_shop
        
        quality_sensor1 = onto.QualitySensor("QualitySensor_H001")
        quality_sensor1.hasName = "Ultrasonic Tester - Hull"
        quality_sensor1.hasID = "QS-H001"
        quality_sensor1.installedOn = hull1
        quality_sensor1.monitors = hull1
        
        # ====================================================================
        # CREATE WORKFORCE
        # ====================================================================
        
        welder1 = onto.Welder("Welder_001")
        welder1.hasName = "John Smith"
        welder1.hasID = "W-001"
        welder1.hasExperience = 15  # years
        welder1.hasCertification = ["AWS D1.1", "6G Position"]
        welder1.locatedAt = "welding_shop"
        
        welder2 = onto.Welder("Welder_002")
        welder2.hasName = "Maria Garcia"
        welder2.hasID = "W-002"   
        welder2.hasExperience = 12
        welder2.hasCertification = ["AWS D1.1"]
        welder2.locatedAt = "welding_shop"
        
        electrician1 = onto.Electrician("Electrician_001")
        electrician1.hasName = "David Chen"
        electrician1.hasID = "E-001"
        electrician1.hasExperience = 10
        electrician1.hasCertification = ["Master Electrician", "Marine Systems"]
        electrician1.locatedAt = "drydock1"
        
        painter1 = onto.Painter("Painter_001")
        painter1.hasName = "Ahmed Hassan"
        painter1.hasID = "P-001"  
        painter1.hasExperience = 8
        painter1.hasCertification = ["NACE Coating Inspector"]
        painter1.locatedAt = "painting_shop"
        
        engineer1 = onto.Engineer("Engineer_001")
        engineer1.hasName = "Dr. Sarah Johnson"
        engineer1.hasID = "ENG-001"
        engineer1.hasExperience = 20
        engineer1.hasCertification = ["Naval Architect", "PE License"]
        
        inspector1 = onto.QualityInspector("Inspector_001")
        inspector1.hasName = "Robert Lee"
        inspector1.hasID = "QI-001"
        inspector1.hasExperience = 18
        inspector1.hasCertification = ["ASNT Level III", "ISO 9001 Lead Auditor"]
        
        safety_officer1 = onto.SafetyOfficer("SafetyOfficer_001")
        safety_officer1.hasName = "Lisa Brown"
        safety_officer1.hasID = "SO-001"
        safety_officer1.hasExperience = 12
        safety_officer1.hasCertification = ["OSHA 30", "CSP"]
        
        manager1 = onto.Manager("Manager_001")
        manager1.hasName = "Michael Anderson"
        manager1.hasID = "MGR-001"
        manager1.hasExperience = 25
        manager1.locatedAt = "office1"
        
        # ====================================================================
        # CREATE PROCESSES
        # ====================================================================
        
        welding_proc1 = onto.WeldingProcess("WeldingProc_H001")
        welding_proc1.hasName = "Hull Welding - Section A"
        welding_proc1.hasID = "WP-H001"
        welding_proc1.hasStatus = "In Progress"
        welding_proc1.hasCompletionPercentage = 75.0
        welding_proc1.hasPriority = "High"
        welding_proc1.hasTemperature = 850.0
        welding_proc1.operatedBy = welder1
        welding_proc1.supervisedBy = engineer1
        welding_proc1.produces = hull1
        welding_proc1.requires = welding_robot1
        
        assembly_proc1 = onto.AssemblyProcess("AssemblyProc_E001")
        assembly_proc1.hasName = "Engine Installation"
        assembly_proc1.hasID = "AP-E001"
        assembly_proc1.hasStatus = "Scheduled"
        assembly_proc1.hasCompletionPercentage = 0.0
        assembly_proc1.hasPriority = "Medium"
        assembly_proc1.supervisedBy = engineer1
        assembly_proc1.produces = vessel1
        assembly_proc1.requires = crane1
        
        inspection_proc1 = onto.InspectionProcess("InspectionProc_H001")
        inspection_proc1.hasName = "Hull Quality Inspection"
        inspection_proc1.hasID = "IP-H001"
        inspection_proc1.hasStatus = "Completed"
        inspection_proc1.hasCompletionPercentage = 100.0
        inspection_proc1.inspectedBy = inspector1
        
        painting_proc1 = onto.PaintingProcess("PaintingProc_V001")
        painting_proc1.hasName = "Hull Surface Coating"
        painting_proc1.hasID = "PP-V001"
        painting_proc1.hasStatus = "Pending"
        painting_proc1.hasCompletionPercentage = 0.0
        painting_proc1.hasPriority = "Low"
        painting_proc1.operatedBy = painter1
        painting_proc1.produces = hull1
        
        # ====================================================================
        # CREATE MATERIALS
        # ====================================================================
        
        steel_plates = onto.SteelPlate("SteelPlate_Stock")
        steel_plates.hasName = "High-Strength Steel Plates"
        steel_plates.hasID = "MAT-SP-001"
        steel_plates.hasQuantity = 500  # units
        steel_plates.locatedAt = "warehouse1"
        steel_plates.usedIn = welding_proc1
        
        welding_rods = onto.WeldingRod("WeldingRod_Stock")
        welding_rods.hasName = "E7018 Welding Electrodes"
        welding_rods.hasID = "MAT-WR-001"
        welding_rods.hasQuantity = 10000
        welding_rods.locatedAt = "warehouse1"
        welding_rods.usedIn = welding_proc1
        
        paint_stock = onto.Paint("Paint_Stock")
        paint_stock.hasName = "Marine Grade Anti-Fouling Paint"
        paint_stock.hasID = "MAT-PT-001"
        paint_stock.hasQuantity = 5000  # liters
        paint_stock.locatedAt = "warehouse1"
        paint_stock.usedIn = painting_proc1
        
        cables = onto.ElectricalCable("Cable_Stock")
        cables.hasName = "Marine Grade Electrical Cable"
        cables.hasID = "MAT-EC-001"
        cables.hasQuantity = 15000  # meters
        cables.locatedAt = "warehouse1"
        
        # ====================================================================
        # CREATE DIGITAL SYSTEMS
        # ====================================================================
        
        mes_system = onto.MES("MES_System")
        mes_system.hasName = "Manufacturing Execution System"
        mes_system.hasID = "DIG-MES-001"
        mes_system.manages = [welding_proc1, assembly_proc1, painting_proc1]
        
        erp_system = onto.ERP("ERP_System")
        erp_system.hasName = "Enterprise Resource Planning"
        erp_system.hasID = "DIG-ERP-001"
        erp_system.manages = [steel_plates, welding_rods, paint_stock, cables]
        
        digital_twin1 = onto.DigitalTwin("DigitalTwin_V001")
        digital_twin1.hasName = "Digital Twin - Pacific Star"
        digital_twin1.hasID = "DIG-DT-V001"
        
        ai_system1 = onto.AISystem("AI_Optimization")
        ai_system1.hasName = "AI Production Optimizer"
        ai_system1.hasID = "DIG-AI-001"
        ai_system1.manages = [welding_proc1, assembly_proc1]
    
    print("✓ Sample data populated")
    return onto


# ============================================================================
# QUERY AND ANALYSIS FUNCTIONS
# ============================================================================

def query_vessels(onto):
    """Query all vessels and their status."""
    
    print("\n" + "="*80)
    print("VESSEL CONSTRUCTION STATUS")
    print("="*80)
    
    for vessel in onto.Vessel.instances():
        print(f"\n🚢 {vessel.hasName if hasattr(vessel, 'hasName') and vessel.hasName is not None else vessel.name}")
        print(f"   ID: {vessel.hasID if hasattr(vessel, 'hasID') and vessel.hasID is not None else 'N/A'}")
        print(f"   Type: {vessel.hasVesselType if hasattr(vessel, 'hasVesselType') and vessel.hasVesselType is not None else 'N/A'}")
        print(f"   Length: {vessel.hasLength if hasattr(vessel, 'hasLength') and vessel.hasLength is not None else 'N/A'} meters")
        print(f"   Deadweight: {vessel.hasDeadweight if hasattr(vessel, 'hasDeadweight') and vessel.hasDeadweight is not None else 'N/A'} tons")
        print(f"   Completion: {vessel.hasCompletionPercentage if hasattr(vessel, 'hasCompletionPercentage') and vessel.hasCompletionPercentage is not None else 'N/A'}%")
        print(f"   Status: {vessel.hasStatus if hasattr(vessel, 'hasStatus') and vessel.hasStatus is not None else 'N/A'}")
        
        if vessel.locatedIn:
            location = vessel.locatedIn
            print(f"   Location: {location.hasName if hasattr(location, 'hasName') and location.hasName is not None else location.name}")
        
        # Show components
        components = [c for c in onto.VesselComponent.instances() if vessel in c.partOf]
        if components:
            print(f"   Components: {len(components)}")
            for comp in components:
                comp_name = comp.hasName if hasattr(comp, 'hasName') and comp.hasName is not None else comp.name
                quality = comp.hasQualityScore   if hasattr(comp, 'hasQualityScore') and comp.hasQualityScore is not None else 'N/A'
                print(f"      • {comp_name} (Quality: {quality})")


def query_workforce(onto):
    """Query workforce distribution."""
    
    print("\n" + "="*80)
    print("WORKFORCE OVERVIEW")
    print("="*80)
    
    worker_types = {
        "Welders": onto.Welder,
        "Electricians": onto.Electrician,
        "Painters": onto.Painter,
        "Engineers": onto.Engineer,
        "Quality Inspectors": onto.QualityInspector,
        "Safety Officers": onto.SafetyOfficer,
        "Managers": onto.Manager
    }
    
    for role, worker_class in worker_types.items():
        workers = list(worker_class.instances())
        print(f"\n{role}: {len(workers)}")
        for worker in workers:
            name = worker.hasName if hasattr(worker, 'hasName') and worker.hasName is not None else worker.name
            exp = worker.hasExperience if hasattr(worker, 'hasExperience') and worker.hasExperience is not None else 'N/A'
            certs = ", ".join(worker.hasCertification) if hasattr(worker, 'hasCertification') and worker.hasCertification is not None else 'None'
            location = worker.locatedIn.hasName if hasattr(worker, 'locatedIn') and worker.locatedIn is not None and hasattr(worker.locatedIn, 'hasName') and worker.locatedIn.hasName is not None else 'N/A'
            print(f"   • {name} (Exp: {exp} years, Location: {location})")
            if certs != 'None':
                print(f"     Certifications: {certs}")


def query_iot_sensors(onto):
    """Query IoT sensor deployment."""
    
    print("\n" + "="*80)
    print("IoT SENSOR NETWORK")
    print("="*80)
    
    sensor_types = {
        "Temperature Sensors": onto.TemperatureSensor,
        "Vibration Sensors": onto.VibrationSensor,
        "Pressure Sensors": onto.PressureSensor,
        "Humidity Sensors": onto.HumiditySensor,
        "Position Sensors": onto.PositionSensor,
        "Safety Sensors": onto.SafetySensor,
        "Quality Sensors": onto.QualitySensor
    }
    
    total_sensors = 0
    for sensor_type, sensor_class in sensor_types.items():
        sensors = list(sensor_class.instances())
        total_sensors += len(sensors)
        if sensors:
            print(f"\n{sensor_type}: {len(sensors)}")
            for sensor in sensors:
                name = sensor.hasName[0] if sensor.hasName else sensor.name
                sensor_id = sensor.hasID[0] if sensor.hasID else 'N/A'
                
                # Get monitoring target
                target = "N/A"
                if sensor.monitors:
                    target_obj = sensor.monitors
                    target = target_obj.hasName if hasattr(target_obj, 'hasName') and target_obj.hasName is not None else target_obj.name
                
                print(f"   • {name} (ID: {sensor_id})")
                print(f"     Monitoring: {target}")
                
                # Show sensor readings
                if hasattr(sensor, 'hasTemperature') and sensor.hasTemperature:
                    print(f"     Reading: {sensor.hasTemperature}°C")
                elif hasattr(sensor, 'hasVibration') and sensor.hasVibration:
                    print(f"     Reading: {sensor.hasVibration} mm/s")
                elif hasattr(sensor, 'hasCoordinates') and sensor.hasCoordinates:
                    print(f"     Coordinates: {sensor.hasCoordinates}")
    
    print(f"\n📊 Total Sensors Deployed: {total_sensors}")


def query_active_processes(onto):
    """Query active manufacturing processes."""
    
    print("\n" + "="*80)
    print("ACTIVE MANUFACTURING PROCESSES")
    print("="*80)
    
    process_types = {
        "Welding": onto.WeldingProcess,
        "Assembly": onto.AssemblyProcess,
        "Inspection": onto.InspectionProcess,
        "Painting": onto.PaintingProcess,
        "Maintenance": onto.MaintenanceProcess
    }
    
    for proc_type, proc_class in process_types.items():
        processes = list(proc_class.instances())
        if processes:
            print(f"\n{proc_type} Processes: {len(processes)}")
            for proc in processes:
                name = proc.hasName if hasattr(proc, 'hasName') and proc.hasName is not None else proc.name
                status = proc.hasStatus if hasattr(proc, 'hasStatus') and proc.hasStatus is not None else 'N/A'
                completion = proc.hasCompletionPercentage  if hasattr(proc, 'hasCompletionPercentage') and proc.hasCompletionPercentage is not None else 0
                priority = proc.hasPriority if hasattr(proc, 'hasPriority') and proc.hasPriority is not None else 'N/A'
                
                print(f"\n   📋 {name}")
                print(f"      Status: {status}")
                print(f"      Completion: {completion}%")
                print(f"      Priority: {priority}")
                
                # Show operator
                if proc.operatedBy:
                    operator = proc.operatedBy if hasattr(proc, 'operatedBy') else None
                    op_name = operator.hasName if hasattr(operator, 'hasName') and operator.hasName is not None else operator.name
                    print(f"      Operator: {op_name}")
                
                # Show supervisor
                if proc.supervisedBy:
                    supervisor = proc.supervisedBy if hasattr(proc, 'supervisedBy') else None
                    sup_name = supervisor.hasName if hasattr(supervisor, 'hasName') and supervisor.hasName is not None else supervisor.name
                    print(f"      Supervisor: {sup_name}")
                
                # Show required equipment
                if proc.requires:
                    equipment = proc.requires if hasattr(proc, 'requires') else None
                    eq_name = equipment.hasName if hasattr(equipment, 'hasName') and equipment.hasName is not None else equipment.name
                    print(f"      Equipment: {eq_name}")


def query_inventory(onto):
    """Query material inventory."""
    
    print("\n" + "="*80)
    print("MATERIAL INVENTORY")
    print("="*80)
    
    materials = list(onto.Material.instances())
    
    for material in materials:
        name = material.hasName if hasattr(material, 'hasName') and material.hasName is not None else material.name
        mat_id = material.hasID if hasattr(material, 'hasID') and material.hasID is not None else 'N/A'
        quantity = material.hasQuantity if hasattr(material, 'hasQuantity') and material.hasQuantity is not None else 0
        
        location = "N/A"
        if material.locatedIn:
            loc_obj = material.locatedIn
            location = loc_obj.hasName if hasattr(loc_obj, 'hasName') and loc_obj.hasName is not None else loc_obj.name
        
        print(f"\n📦 {name}")
        print(f"   ID: {mat_id}")
        print(f"   Quantity: {quantity}")
        print(f"   Location: {location}")
        
        # Show where used
        if material.usedIn:
            proc = material.usedIn
            print(f"   Used in processes:")
            proc_name = proc.hasName if hasattr(proc, 'hasName') and proc.hasName is not None else proc.name
            print(f"      • {proc_name}")


def query_equipment_status(onto):
    """Query equipment operational status."""
    
    print("\n" + "="*80)
    print("EQUIPMENT STATUS")
    print("="*80)
    
    equipment_types = {
        "Cranes": onto.Crane,
        "Welding Robots": onto.WeldingRobot,
        "Cutting Machines": onto.CuttingMachine,
        "Transport Vehicles": onto.TransportVehicle
    }
    
    for eq_type, eq_class in equipment_types.items():
        equipment_list = list(eq_class.instances())
        if equipment_list:
            print(f"\n{eq_type}: {len(equipment_list)}")
            for eq in equipment_list:
                name = eq.hasName[0] if eq.hasName else eq.name
                eq_id = eq.hasID if hasattr(eq, 'hasID') and eq.hasID is not None else 'N/A'
                status = eq.hasStatus if hasattr(eq, 'hasStatus') and eq.hasStatus is not None else 'Unknown'
                capacity = eq.hasCapacity if hasattr(eq, 'hasCapacity') and eq.hasCapacity is not None else 'N/A'
                
                location = "N/A"
                if eq.locatedIn:
                    loc_obj = eq.locatedIn
                    location = loc_obj.hasName if hasattr(loc_obj, 'hasName') and loc_obj.hasName is not None else loc_obj.name
                
                print(f"\n   ⚙️  {name}")
                print(f"      ID: {eq_id}")
                print(f"      Status: {status}")
                print(f"      Capacity: {capacity}")
                print(f"      Location: {location}")
                
                # Show attached sensors
                sensors = [s for s in onto.Sensor.instances() if hasattr(s, 'installedOn') and s.installedOn == eq]
                if sensors:
                    print(f"      Sensors: {len(sensors)}") 
                    for sensor in sensors:
                        sensor_name = sensor.hasName if hasattr(sensor, 'hasName') and sensor.hasName is not None   else sensor.name
                        print(f"         • {sensor_name}")


def query_digital_systems(onto):
    """Query digital infrastructure."""
    
    print("\n" + "="*80)
    print("DIGITAL SYSTEMS & SMART TECHNOLOGIES")
    print("="*80)
    
    system_types = {
        "MES (Manufacturing Execution)": onto.MES,
        "ERP (Enterprise Resource Planning)": onto.ERP,
        "Digital Twins": onto.DigitalTwin,
        "AI/ML Systems": onto.AISystem
    }
    
    for sys_type, sys_class in system_types.items():
        systems = list(sys_class.instances())
        if systems:
            print(f"\n{sys_type}: {len(systems)}")
            for system in systems:
                name = system.hasName[0] if system.hasName else system.name
                sys_id = system.hasID[0] if system.hasID else 'N/A'
                
                print(f"\n   💻 {name}")
                print(f"      ID: {sys_id}")
                
                # Show what it manages
                if system.manages:
                    print(f"      Managing {len(system.manages)} entities:")
                    for managed in system.manages[:5]:  # Show first 5
                        managed_name = managed.hasName[0] if managed.hasName else managed.name
                        print(f"         • {managed_name}")
                    if len(system.manages) > 5:
                        print(f"         ... and {len(system.manages) - 5} more")


def generate_shipyard_analytics(onto):
    """Generate analytics and KPIs."""
    
    print("\n" + "="*80)
    print("SHIPYARD ANALYTICS & KPIs")
    print("="*80)
    
    # Count entities
    total_vessels = len(list(onto.Vessel.instances()))
    total_workers = len(list(onto.Worker.instances()))
    total_equipment = len(list(onto.Equipment.instances()))
    total_sensors = len(list(onto.Sensor.instances()))
    total_processes = len(list(onto.Process.instances()))
    
    print(f"\n📊 Key Metrics:")
    print(f"   Vessels under construction: {total_vessels}")
    print(f"   Total workforce: {total_workers}")
    print(f"   Equipment units: {total_equipment}")
    print(f"   IoT sensors deployed: {total_sensors}")
    print(f"   Active processes: {total_processes}")
    
    # Calculate average completion
    vessels = list(onto.Vessel.instances())
    if vessels:
        avg_completion = sum(v.hasCompletionPercentage if hasattr(v, 'hasCompletionPercentage') and v.hasCompletionPercentage is not None else 0 for v in vessels) / len(vessels)
        print(f"   Average vessel completion: {avg_completion:.1f}%")
    
    # Process status breakdown
    processes = list(onto.Process.instances())
    status_count = {}
    for proc in processes:
        status = proc.hasStatus[0] if proc.hasStatus else 'Unknown'
        status_count[status] = status_count.get(status, 0) + 1
    
    print(f"\n📈 Process Status Distribution:")
    for status, count in status_count.items():
        print(f"   {status}: {count}")
    
    # Equipment utilization
    equipment = list(onto.Equipment.instances())
    operational = sum(1 for eq in equipment if eq.hasStatus and eq.hasStatus[0] == 'Operational')
    utilization = (operational / len(equipment) * 100) if equipment else 0
    
    print(f"\n⚙️  Equipment Utilization:")
    print(f"   Operational: {operational}/{len(equipment)} ({utilization:.1f}%)")
    
    # Quality metrics
    components = list(onto.VesselComponent.instances())
    components_with_quality = [c for c in components if c.hasQualityScore]
    if components_with_quality:
        avg_quality = sum(c.hasQualityScore if hasattr(c, 'hasQualityScore') and c.hasQualityScore is not None else 0 for c in components_with_quality) / len(components_with_quality)
        print(f"\n✅ Quality Metrics:")
        print(f"   Average component quality score: {avg_quality:.1f}/100")


def save_ontology(onto):
    """Save the ontology to file."""
    
    print("\n" + "="*80)
    print("SAVING ONTOLOGY")
    print("="*80)
    
    onto.save(file="smart_shipyard.owl", format="rdfxml")
    print("✓ Ontology saved to 'smart_shipyard.owl'")
    print("\nYou can open this file with:")
    print("  • Protégé: https://protege.stanford.edu/")
    print("  • WebVOWL: http://vowl.visualdataweb.org/webvowl.html")


# ============================================================================
# ADVANCED QUERIES
# ============================================================================

def find_vessels_by_completion(onto, min_completion=50):
    """Find vessels with completion above threshold."""
    
    print(f"\n🔍 Vessels with >{min_completion}% completion:")
    for vessel in onto.Vessel.instances():
        if vessel.hasCompletionPercentage and vessel.hasCompletionPercentage > min_completion:
            name = vessel.hasName if hasattr(vessel, 'hasName') and vessel.hasName is not None else vessel.name
            completion = vessel.hasCompletionPercentage
            print(f"   • {name}: {completion}%")


def find_experienced_workers(onto, min_years=10):
    """Find workers with experience above threshold."""
    
    print(f"\n🔍 Workers with >{min_years} years experience:")
    for worker in onto.Worker.instances():
        if worker.hasExperience and worker.hasExperience > min_years:
            name = worker.hasName if hasattr(worker, 'hasName') and worker.hasName is not None else worker.name
            exp = worker.hasExperience
            worker_type = type(worker).__name__
            print(f"   • {name} ({worker_type}): {exp} years")


def find_high_priority_processes(onto):
    """Find high priority processes."""
    
    print(f"\n🔍 High Priority Processes:")
    for process in onto.Process.instances():
        if process.hasPriority and process.hasPriority[0] == "High":
            name = process.hasName[0] if process.hasName else process.name
            status = process.hasStatus[0] if process.hasStatus else 'N/A'
            completion = process.hasCompletionPercentage[0] if process.hasCompletionPercentage else 0
            print(f"   • {name}")
            print(f"     Status: {status}, Completion: {completion}%")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    
    print("\n" + "="*80)
    print("SMART SHIPYARD ONTOLOGY SYSTEM")
    print("Comprehensive Digital Twin for Shipyard 4.0")
    print("="*80)
    
    # Create and populate ontology
    onto = create_smart_shipyard_ontology()
    onto = populate_shipyard_data(onto)
    
    # Execute queries
    query_vessels(onto)
    query_workforce(onto)
    query_iot_sensors(onto)
    query_active_processes(onto)
    query_equipment_status(onto)
    query_inventory(onto)
    query_digital_systems(onto)
    
    # Analytics
    generate_shipyard_analytics(onto)
    
    # Advanced queries
    print("\n" + "="*80)
    print("ADVANCED QUERIES")
    print("="*80)
    find_vessels_by_completion(onto, min_completion=50)
    find_experienced_workers(onto, min_years=10)
    find_high_priority_processes(onto)
    
    # Save ontology
    save_ontology(onto)
    
    print("\n" + "="*80)
    print("SMART SHIPYARD ONTOLOGY SYSTEM - COMPLETED")
    print("="*80)
    print("\nKey Features Demonstrated:")
    print("  ✓ Vessel construction management")
    print("  ✓ IoT sensor network integration")
    print("  ✓ Workforce and skills tracking")
    print("  ✓ Manufacturing process monitoring")
    print("  ✓ Equipment status tracking")
    print("  ✓ Material inventory management")
    print("  ✓ Digital systems integration (MES, ERP, Digital Twin, AI)")
    print("  ✓ Quality control and inspection")
    print("  ✓ Safety monitoring")
    print("  ✓ Analytics and KPIs")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()