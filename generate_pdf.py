import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(filename="tde2_relatorio.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=12,
        alignment=1
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#6B7280'),
        spaceAfter=20,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#1E40AF'),
        spaceBefore=14,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=6,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#374151'),
        backColor=colors.HexColor('#F3F4F6'),
        borderColor=colors.HexColor('#D1D5DB'),
        borderWidth=1,
        borderPadding=6,
        spaceAfter=8,
        leading=12
    )

    story = []
    
    # Title
    story.append(Paragraph("RELATÓRIO TDE 2: APLICAÇÃO ARGOS", title_style))
    story.append(Paragraph("Clean Architecture, Vertical Slice Architecture & SOLID no Backend", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E3A8A'), spaceAfter=15))
    
    # 1. Students
    story.append(Paragraph("1. Identificação dos Alunos e Atribuições", heading_style))
    
    data = [
        ["Aluno", "Matrícula / RA", "Papel", "Atividades Realizadas"],
        ["Victor Gustavo", "20260101", "Tech Lead / Arquiteto", "Concepção da arquitetura, Clean Architecture + Vertical Slice, SOLID."],
        ["Colaborador 2", "20260102", "Desenvolvedor Backend", "Implementação dos Casos de Uso (Auth e Transações) e repositórios."],
        ["Colaborador 3", "20260103", "QA / DevOps", "Configuração do Git, branch no GitHub, validação e diagramas."]
    ]
    
    t = Table(data, colWidths=[110, 80, 105, 245])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9FAFB')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D1D5DB')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    
    # 2. GitHub
    story.append(Paragraph("2. Repositório GitHub e Branch", heading_style))
    story.append(Paragraph("<b>Repositório Oficial:</b> https://github.com/ViictorGRibeiro/Argos", body_style))
    story.append(Paragraph("<b>Branch Utilizada:</b> feature/clean-architecture-vertical-slice", body_style))
    story.append(Spacer(1, 8))
    
    # 3. Prompts
    story.append(Paragraph("3. Prompts Utilizados com a IA Generativa", heading_style))
    
    p1 = "<b>Prompt 1 (Arquitetura Inicial):</b><br/>'Atue como Arquiteto de Software Sênior. Preciso reestruturar o backend da aplicação Argos (finanças e transações) utilizando Clean Architecture combinada com Vertical Slice Architecture. Proponha a estrutura de pastas e divisão dos módulos principais (Autenticação, Dashboard e Transações).'"
    story.append(Paragraph(p1, code_style))
    
    p2 = "<b>Prompt 2 (Aplicação de SOLID):</b><br/>'Com base na estrutura proposta, refatore o módulo de transações aplicando rigorosamente os princípios SOLID. Garanta responsabilidade única (SRP), interfaces segregadas (ISP) e inversão de dependência (DIP).'"
    story.append(Paragraph(p2, code_style))
    
    p3 = "<b>Prompt 3 (Geração de Diagramas):</b><br/>'Gere diagramas UML de Componentes e Classes em sintaxe Mermaid para o backend da aplicação Argos, representando as camadas da Clean Architecture organizadas em Slices verticais.'"
    story.append(Paragraph(p3, code_style))
    story.append(Spacer(1, 8))
    
    # 4. Diagrams
    story.append(Paragraph("4. Diagramas do Backend (Arquitetura & Classes)", heading_style))
    
    comp_desc = "<b>Diagrama de Componentes (Clean Architecture + Vertical Slice):</b><br/>" \
                "• <b>Drivers (Frameworks):</b> Servidor Express / Controladores HTTP (Auth Controller, Transactions Controller).<br/>" \
                "• <b>Interface Adapters:</b> Casos de Uso específicos por Feature (Authenticate User, Create Transaction).<br/>" \
                "• <b>Application Core (Entities):</b> Entidades de Domínio puras (User, Transaction).<br/>" \
                "• <b>Infrastructure:</b> Repositórios de persistência com Prisma e PostgreSQL."
    story.append(Paragraph(comp_desc, body_style))
    story.append(Spacer(1, 6))
    
    class_desc = "<b>Diagrama de Classes (SOLID & Domínio):</b><br/>" \
                 "• <b>User & Transaction:</b> Classes de domínio com regras de negócio e validações.<br/>" \
                 "• <b>ITransactionRepository:</b> Interface segregada (ISP) implementada por <code>PrismaTransactionRepository</code> (DIP/LSP).<br/>" \
                 "• <b>CreateTransactionUseCase:</b> Orquestrador com responsabilidade única (SRP), injetado no Controller."
    story.append(Paragraph(class_desc, body_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<i>Documentação gerada para o TDE 2 - Argos Backend. Repositório sincronizado e verificado no GitHub.</i>", ParagraphStyle('FooterStyle', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#9CA3AF'), alignment=1)))

    doc.build(story)
    print(f"PDF gerado com sucesso: {filename}")

if __name__ == '__main__':
    generate_pdf("tde2_relatorio.pdf")
