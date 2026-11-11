from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Float  
from sqlalchemy import DateTime
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    qualification = Column(String)
    location = Column(String)

class StudentSkill(Base):
    __tablename__ = "student_skills"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    skill_name = Column(String, nullable=False)

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    company_name = Column(String, nullable=False)
    location = Column(String)
    industry = Column(String)

class Internship(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    required_qualification = Column(String)
    location = Column(String)
    duration = Column(String)
    available_seats = Column(Integer, nullable=False)

class InternshipSkill(Base):
    __tablename__ = "internship_skills"

    id = Column(Integer, primary_key=True, index=True)
    internship_id = Column(
        Integer,
        ForeignKey("internships.id"),
        nullable=False
    )
    skill_name = Column(String, nullable=False)

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    internship_id = Column(
        Integer,
        ForeignKey("internships.id"),
        nullable=False
    )

    status = Column(String, default="applied", nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "internship_id",
            name="uq_student_internship_application"
        ),
    )

class MatchScore(Base):
    __tablename__ = "match_scores"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    internship_id = Column(
        Integer,
        ForeignKey("internships.id"),
        nullable=False
    )

    keyword_score = Column(Float, default=0.0)
    multifactor_score = Column(Float, default=0.0)
    semantic_score = Column(Float, default=0.0)
    total_score = Column(Float, default=0.0)

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "internship_id",
            name="uq_student_internship_match"
        ),
    )

class Allocation(Base):
    __tablename__ = "allocations"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    internship_id = Column(
        Integer,
        ForeignKey("internships.id"),
        nullable=False
    )

    status = Column(String, default="allocated", nullable=False)

    allocated_at = Column(DateTime, default=datetime.utcnow)